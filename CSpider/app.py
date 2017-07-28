# -*- coding:utf-8 -*-

import logging
from functools import partial
from concurrent.futures import ThreadPoolExecutor

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from urls import handlers
from urls import settings
from Database import db
from Conf.config import config
from Conf.options import default_options
from Service.Monitor import Monitor
from Database.models import SpiderTask
from Utils.SpiderWorkers import spider_worker
from Manager.SpiderManager import SpiderManager
from Manager.ServiceManager import ServiceManager

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/6/27'
__Version__ = '0.1'

"""
    Initialize Application
"""


class Application(tornado.web.Application):
    monitor_pool_default = ThreadPoolExecutor
    monitor_pool_worker = 4

    _service = ['monitor']

    def __init__(self):
        super(Application, self).__init__(handlers=handlers, **settings)
        # Extra Configuration
        self.extra_config = config['default']

        self.io_loop = tornado.ioloop.IOLoop.instance()
        self.db = db

        # Log
        self.log = logging

        # Spiders
        self.spiders = SpiderManager().spiders

        # Services
        self.inner_services = ServiceManager()

        # Monitor
        self.c_app = spider_worker
        self.monitor = Monitor(c_app=self.c_app, io_loop=self.io_loop, config=self.extra_config['MONITOR'],
                               log=self.log)
        self.monitor_pool = self.monitor_pool_default(max_workers=self.monitor_pool_worker)

    def run(self):
        """ Server Start """

        try:
            self.task_status_reset()
            self.register_service()
            tornado.options.parse_command_line()
            self.start_log_msg()
            server = tornado.httpserver.HTTPServer(self)
            server.listen(default_options.port)
            self.io_loop.start()
        except Exception as err:
            self.log.error(str(err))

    def register_service(self):
        """ Register Service In Application """

        for service in self._service:
            if getattr(getattr(self, service), 'start', None):
                getattr(self, service).start(flag=True)
            self.inner_services.register_service(getattr(self, service))

    def delay(self, method, *args, **kwargs):
        """ Query Monitor's Info """

        return self.monitor_pool.submit(partial(method, *args, **kwargs))

    def start_log_msg(self):
        """ Server Start Output Info """

        self.log.info('-' * 48)
        self.log.info('|' + ' ' * 46 + '|')
        self.log.info('|' + ' ' * 19 + 'CSpider ' + ' ' * 19 + '|')
        self.log.info('|' + ' ' * 46 + '|')

        self.log.info('-' * 15 + ' AutoLoad Spiders ' + '-' * 15)
        for _ in sorted(self.spiders.keys()):
            self.log.info(' ' + _ + ' ' * (47 - len(_) - 16) + 'Initial Success')
        self.log.info('')

        if self.inner_services:
            self.log.info('-' * 12 + ' Auto Register Services ' + '-' * 12)
            for key, value in self.inner_services.services.items():
                if value:
                    self.log.info(' ' + key + ' ' * (47 - len(key) - 14) + 'Start Success')
                else:
                    self.log.info(' ' + key + ' ' * (47 - len(key) - 9) + 'No Start')
            self.log.info('-' * 48)

    def task_status_reset(self):
        """ Reset Spider Task Status When Application Start """

        tasks = self.db.session.query(SpiderTask).filter_by(status='running').all()
        if tasks:
            for task in tasks:
                task.status = 'stop'
            self.db.session.commit()

if __name__ == '__main__':
    Application().run()
    # Application().db.init_db()
