# -*- utf-8 -*-

from tornado import gen

from Utils.BaseHandle import BaseHandler

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/4'
__Version__ = '0.1'


class SpiderTaskHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        self.render('task.html')
