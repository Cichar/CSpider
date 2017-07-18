# -*- coding:utf-8 -*-

from tornado import gen

from Utils.BaseHandle import BaseHandler
from Manager.SpiderManager import SpiderManager

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/2'
__Version__ = '0.1'


class SpidersHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        """ From SpiderManager Getting Spiders, 
            Then Pass Spider Objects To The Web To Render Spider  
        """

        spiders = SpiderManager().spiders
        return self.render("spiders.html", spiders=spiders)
