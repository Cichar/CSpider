# -*- coding:utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from urls import handlers
from urls import settings
from Database import db
from Conf.options import default_options

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
        try:
            print('** %s Client Start! **' % __Author__)
            tornado.options.parse_command_line()
            server = tornado.httpserver.HTTPServer(self)
            server.listen(default_options.port)
            self.io_loop.start()
        except Exception as err:
            print(err)

if __name__ == '__main__':
    Application().run()
