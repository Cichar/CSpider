# -*- utf-8 -*-

from tornado import gen

from Utils.BaseHandle import BaseHandler
from Manager.SpiderManager import SpiderManager

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/4'
__Version__ = '0.1'


class SpiderTaskHandler(BaseHandler):
    @gen.coroutine
    def get(self, spider):
        try:
            form = SpiderManager().spiders[spider]['form']
            print(form)
        except Exception as err:
            print(err)
        else:
            self.render('task.html', form=form)

    @gen.coroutine
    def post(self):
        self.write('success')