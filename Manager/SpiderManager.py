# -*- coding:utf-8 -*-

try:
    import Spider
except Exception as err:
    print(err)

from Utils.Singleton import Singleton
from Utils.BaseSpider import BaseSpider

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/1'
__Version__ = '0.1'


class SpiderManager(object, metaclass=Singleton):
    """ Spider Manager """

    def __init__(self):
        self.spiders = BaseSpider.__subclasses__()
