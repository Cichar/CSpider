# -*- utf-8 -*-

from Manager.SpiderManager import SpiderManager
from Utils.BaseHandle import BaseHandler
from tornado import gen

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/4'
__Version__ = '0.1'


class SpiderTaskHandler(BaseHandler):
    @gen.coroutine
    def get(self, spider):
        try:
            form = SpiderManager().spiders[spider]['form']()
        except Exception as err:
            print(err)
        else:
            self.render('task.html', form=form)

    @gen.coroutine
    def post(self, spider_name):
        try:
            spider_dict = SpiderManager().spiders[spider_name]
            form = spider_dict['form'](self.request.arguments)
            spider_dict['spider'].task_distribute(form.data)
            self.write(form.data)
        except Exception as err:
            print(err)
