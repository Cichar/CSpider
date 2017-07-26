# -*- coding:utf-8 -*-

from tornado import gen

from Database.models import SpiderTask
from Utils.BaseHandle import BaseHandler

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/6/27'
__Version__ = '0.1'


class IndexHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        tasks = self.query(SpiderTask).all()
        return self.render("index.html", tasks=tasks)
