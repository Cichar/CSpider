# -*- coding:utf-8 -*-

import logging

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from urls import handlers
from urls import settings
from Database import db
from Conf.options import default_options
from Manager.SpiderManager import SpiderManager

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/6/27'
__Version__ = '0.1'

"""
    Initialize Application
"""


class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(handlers=handlers, **settings)
        self.io_loop = tornado.ioloop.IOLoop.instance()
        self.db = db

    def run(self):
        """ Server Start """

        try:
            tornado.options.parse_command_line()
            self.start_log_msg()
            server = tornado.httpserver.HTTPServer(self)
            server.listen(default_options.port)
            self.io_loop.start()
        except Exception as err:
            print(err)

    @staticmethod
    def log(message, level='INFO'):
        """ Log Output """

        if level == 'INFO':
            logging.info(message)
        elif level == 'WARNING':
            logging.warning(message)
        elif level == 'ERROR':
            logging.error(message)
        elif level == 'DEBUG':
            logging.debug(message)

    def start_log_msg(self):
        """ Server Start Output Info """

        self.log('-' * 48)
        self.log('|' + ' ' * 46 + '|')
        self.log('|' + ' ' * 19 + 'CSpider ' + ' ' * 19 + '|')
        self.log('|' + ' ' * 46 + '|')
        self.log('-' * 15 + ' AutoLoad Spiders ' + '-' * 15)
        for _ in SpiderManager().spiders:
            logging.info(' ' + _.name + ' ' * (47 - len(_.name) - 16) + 'Initial Success')

if __name__ == '__main__':
    Application().run()
