# -*- utf-8 -*-

from functools import partial

from tornado import websocket
from tornado.ioloop import PeriodicCallback

from Database.models import SpiderTask

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/26'
__Version__ = '0.1'


class TasksUpdateHandler(websocket.WebSocketHandler):
    listeners = []
    periodic_callback = None
    interval = 2000

    def open(self):
        app = self.application

        if not self.listeners:
            if not self.periodic_callback:
                self.periodic_callback = PeriodicCallback(
                                            partial(self.on_update_time, app),
                                            app.extra_config['TASK']['TASK_UPDATE_INTERVAL'] or self.interval
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
        update = cls.tasks_update(app)
        if update:
            for l in cls.listeners:
                l.write_message(update)

    @classmethod
    def tasks_update(cls, app):
        """ Create Tasks Update Info """

        try:
            tasks_info = {}
            tasks = app.db.session.query(SpiderTask).all()
        except Exception as err:
            print(err)
        else:
            for task in tasks:
                tasks_info[task.id] = task.to_json()
            return tasks_info
        finally:
            app.db.session.close()

    def on_message(self, message):
        pass

    def data_received(self, chunk):
        pass
