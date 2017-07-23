# -*- utf-8 -*-

from tornado import gen

from Utils.BaseHandle import BaseHandler
from Database.models import SpiderTask

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/4'
__Version__ = '0.1'


class SpiderTaskHandler(BaseHandler):
    @gen.coroutine
    def get(self, spider_name):
        """ Choice The Spider Task Form Depend On Spider Name, 
            Then Pass The Form Object To The Web.
        """

        try:
            form = self.spiders[spider_name]['form']()
        except Exception as err:
            print(err)
        else:
            return self.render('task.html', form=form)

    @gen.coroutine
    def post(self, spider_name):
        """ Choice The Spider Depend On Spider Name, 
            Then Pass The Form Data Which Given By User On Web To The Selected Spider, 
            The Spider Uses Form Data To Distribute Tasks.
        """

        try:
            spider_dict = self.spiders[spider_name]
            form = spider_dict['form'](self.request.arguments)

            task = SpiderTask(name=spider_name)
            self.add(task)
            self.commit()

            spider_dict['spider'].task_distribute(form.data, st_id=task.id)
        except Exception as err:
            print(err)
        else:
            return self.write('OK.')
