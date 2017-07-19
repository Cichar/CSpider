# -*- utf-8 -*-

import threading

from functools import partial
from collections import Counter
from collections import defaultdict

import celery
from celery.events.state import State
from tornado.ioloop import PeriodicCallback

from Utils.BaseService import BaseService


class EventsState(State):
    def __init__(self, *args, **kwargs):
        super(EventsState, self).__init__(*args, **kwargs)
        self.counter = defaultdict(Counter)

    def event(self, event):
        """ OverWrite Event Function Which In State Class ,
            To Note Down The Event Info Which Can't Search By The Celery API.
            Such AS: Failed Task, Retried Task And So On.
            
            Example:
                defaultdict(<class 'collections.Counter'>, 
                {'celery@test_worker_1': Counter({'task-received': 7, 'task-started': 7, 
                                                  'task-succeeded': 4, 'worker-heartbeat': 4}), 
                'celery@test_worker_2': Counter({'worker-heartbeat': 4, 'task-received': 4, 
                                                 'task-started': 4, 'task-succeeded': 2})})
        """

        worker_name = event['hostname']
        event_type = event['type']

        self.counter[worker_name][event_type] += 1

        # Pass Event To The Default Event Function
        super(EventsState, self).event(event)


class Monitor(threading.Thread, BaseService):
    events_enable_interval = 5000

    def __init__(self, c_app=None, io_loop=None, enable_events=True, config=None, log=None):
        threading.Thread.__init__(self)

        self.c_app = c_app
        self.io_loop = io_loop
        self.enable_events = enable_events
        self.config = config
        self.log = log

        self.state = EventsState()
        self.queues = self.store_queues()

        self.timer = PeriodicCallback(self.on_enable_events,
                                      self.config.get(
                                          'MONITOR_EVENTS_ENABLE_INTERVAL', None) or self.events_enable_interval)

        self.started = False

    def start(self, flag=False):
        try:
            self.daemon = flag
            threading.Thread.start(self)
            if self.enable_events and celery.VERSION[0] > 2:
                self.timer.start()
        except Exception as err:
            self.started = False
            self.log.error(str(err))
        else:
            self.started = True

    def run(self):
        """ When Call threading.Thread.start() Function , It will Call Run Function.

            Receiver Function Which In ''Celery.events'' Will Use handlers's Key To Be The Event，
            If Pass ''*'' To Be The Key, It Will Pass All The Default Events Those In Celery 
            To The Value Which Is The Callback Function. 
        """

        while True:
            try:
                with self.c_app.connection() as conn:
                    recv = self.c_app.events.Receiver(conn, handlers={'*': self.on_event})
                    recv.capture(limit=None, timeout=None, wakeup=True)
            except Exception as err:
                self.log.error(str(err))

    def on_event(self, event):
        """ Add Callback To The Io_loop To Avoid Synchronization """

        self.io_loop.add_callback(partial(self.state.event, event))

    def on_enable_events(self):
        """ Start Celery Default Events Monitor """

        try:
            self.c_app.control.enable_events()
        except Exception as err:
            self.log.error(str(err))

    def store_queues(self):
        """ From Celery Configuration Load Queues And Return The Queues """

        default_queues = self.c_app.conf.CELERY_QUEUES
        queues = set([])
        for q in default_queues:
            queues.add(q.name)
        return queues
