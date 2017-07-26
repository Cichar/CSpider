# -*- utf-8 -*-

from functools import partial
from collections import defaultdict

from tornado import websocket
from tornado.ioloop import PeriodicCallback

from Service.Monitor.broker import Broker


class MonitorUpdateHandler(websocket.WebSocketHandler):
    listeners = []
    periodic_callback = None
    interval = 2000

    def open(self):
        app = self.application

        if not self.listeners:
            if not self.periodic_callback:
                self.periodic_callback = PeriodicCallback(
                                            partial(self.on_update_time, app),
                                            app.extra_config['MONITOR']['MONITOR_UPDATE_INTERVAL'] or self.interval
                                            )
            if not self.periodic_callback.is_running():
                self.periodic_callback.start()
        self.listeners.append(self)

    def on_close(self):
        """ Close Websocket """

        if self in self.listeners:
            self.listeners.remove(self)
        if not self.listeners and self.periodic_callback:
            self.periodic_callback.stop()

    @classmethod
    def on_update_time(cls, app):
        update = cls.monitor_update(app)
        if update:
            for l in cls.listeners:
                l.write_message(update)

    @staticmethod
    def get_queues_info(c_app=None, queues=None):
        """ Get The Queues Info"""
        broker_options = c_app.conf.BROKER_TRANSPORT_OPTIONS

        broker = Broker(c_app.connection().as_uri(include_password=True), broker_options=broker_options)

        queues_info = broker.queues(queues)
        return queues_info

    @classmethod
    def monitor_update(cls, app):
        """ Create Monitor Update Info """

        events = app.monitor.state
        queues = app.monitor.queues
        workers = {'active': 0, 'queues': '', 'workers': defaultdict(dict)}

        for name, worker in events.workers.items():
            counter = events.counter[name]
            active = getattr(worker, 'active', None)
            processed = counter.get('task-received', 0)
            failed = counter.get('task-failed', 0)
            succeeded = counter.get('task-succeeded', 0)
            retried = counter.get('task-retried', 0)

            workers['workers'][name] = dict(
                name=name,
                status=worker.status_string,
                active=active,
                processed=processed,
                failed=failed,
                succeeded=succeeded,
                retried=retried)
            if worker.status_string == 'ONLINE':
                workers['active'] += int(active)

        # Get The Queues Info
        workers['queues'] = cls.get_queues_info(c_app=app.c_app, queues=queues)
        return workers

    def on_message(self, message):
        pass

    def data_received(self, chunk):
        pass
