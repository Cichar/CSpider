# -*- utf-8 -*-

from tornado import gen

from Utils.BaseHandle import BaseHandler

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/18'
__Version__ = '0.1'


class MonitorHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        app = self.application
        events = app.monitor.state

        workers = {}
        for name, values in events.counter.items():
            worker = events.workers[name]
            info = dict(values)
            info.update(self._as_dict(worker))
            info.update({'status': worker.status_string})
            workers[name] = info
        return self.render('monitor.html', workers=workers)

    @classmethod
    def _as_dict(cls, worker):
        if hasattr(worker, '_fields'):
            return dict((k, worker.__getattribute__(k)) for k in worker._fields)
        else:
            return cls._info(worker)

    @classmethod
    def _info(cls, worker):
        """ If Worker Don't Have _field Attribute 
            Then Use This Function To Create Info 
        """

        _fields = ('hostname', 'pid', 'freq', 'heartbeats', 'clock',
                   'active', 'processed', 'loadavg', 'sw_ident',
                   'sw_ver', 'sw_sys')

        def _keys():
            for key in _fields:
                value = getattr(worker, key, None)
                if value is not None:
                    yield key, value

        return dict(_keys())
