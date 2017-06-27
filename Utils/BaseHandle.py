# -*- coding:utf-8 -*-

from tornado.web import RequestHandler

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/6/27'
__Version__ = '0.1'

"""
    Base Request Handle File
"""


class BaseHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    @property
    def db(self):
        return self.application.db

    def on_finish(self):
        """ 一个请求完成后调用此方法 """
        try:
            pass
        except Exception as err:
            print(err)
        finally:
            self.db.session.close()

    def query(self, model):
        """ 查询数据库 """

        _model = self.db.session.query(model)
        return _model
