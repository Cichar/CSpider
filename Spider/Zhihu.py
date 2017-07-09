# -*- coding:utf-8 -*-

from Utils.BaseSpider import BaseSpider
from Utils.SpiderWorkers import spider_worker

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/1'
__Version__ = '0.1'


class ZhiHuSpider(BaseSpider):
    name = u'ZhiHuUser'

    def task_distribute(self, data):
        self.add.delay(data['target'])

    @staticmethod
    @spider_worker.task
    def add(x):
        return x * 2
