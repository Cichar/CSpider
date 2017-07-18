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
from Utils.SpiderWorkers import spider_worker
from Monitor.monitor import Monitor
from Manager.SpiderManager import SpiderManager

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

    def __init__(self):
        super(Application, self).__init__(handlers=handlers, **settings)
        # Extra Configuration
        self.extra_config = config['default']

        self.io_loop = tornado.ioloop.IOLoop.instance()
        self.db = db

        # Log
        self.log = logging

        # Monitor
        self.c_app = spider_worker
        self.monitor = Monitor(c_app=self.c_app, io_loop=self.io_loop, config=self.extra_config['MONITOR'],
                               log=self.log)
        self.monitor_pool = self.monitor_pool_default(max_workers=self.monitor_pool_worker)

    def run(self):
        """ Server Start """

        try:
            self.monitor.start()
            tornado.options.parse_command_line()
            self.start_log_msg()
            server = tornado.httpserver.HTTPServer(self)
            server.listen(default_options.port)
            self.io_loop.start()
        except Exception as err:
            print(err)

    def start_log_msg(self):
        """ Server Start Output Info """

        self.log.info('-' * 48)
        self.log.info('|' + ' ' * 46 + '|')
        self.log.info('|' + ' ' * 19 + 'CSpider ' + ' ' * 19 + '|')
        self.log.info('|' + ' ' * 46 + '|')
        self.log.info('-' * 15 + ' AutoLoad Spiders ' + '-' * 15)
        for _ in SpiderManager().spiders:
            self.log.info(' ' + _ + ' ' * (47 - len(_) - 16) + 'Initial Success')

    def delay(self, method, *args, **kwargs):
        """ Query Monitor's Info """

        return self.monitor_pool.submit(partial(method, *args, **kwargs))

if __name__ == '__main__':
    Application().run()
    # Application().db.init_db()
