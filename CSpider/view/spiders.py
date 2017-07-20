# -*- coding:utf-8 -*-

from tornado import gen

from Utils.BaseHandle import BaseHandler

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/2'
__Version__ = '0.1'


class SpidersHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        """ From Application Getting Spiders, 
            Then Pass Spider's Name To The Web To Render.  
        """

        spiders = [spider for spider in self.spiders]
        return self.render("spiders.html", spiders=spiders)
