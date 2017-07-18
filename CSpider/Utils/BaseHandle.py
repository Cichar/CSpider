# -*- coding:utf-8 -*-

import tornado.web

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/6/27'
__Version__ = '0.1'

"""
    Base Request Handle File
"""


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def write_error(self, status_code, **kwargs):
        self.db.session.close()
        if status_code in [403, 404, 500]:
            self.render('error\%d.html' % status_code)
        else:
            self.render('error\error.html', status_code=status_code)

    @property
    def db(self):
        return self.application.db

    def on_finish(self):
        """ On Request Finish, Close The Database Session """
        try:
            pass
        finally:
            self.db.session.close()

    def query(self, model):
        """ Database Query Function """

        _model = self.db.session.query(model)
        return _model


class ErrorHandler(tornado.web.ErrorHandler, BaseHandler):
    pass
