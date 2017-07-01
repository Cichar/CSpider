# -*- coding:utf-8 -*-

import os

from tornado.web import url

from view import index
from view import spiders

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/6/27'
__Version__ = '0.1'

settings = {
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    'static_path': os.path.join(os.path.dirname(__file__), "static"),
    'debug': True
}

handlers = [
    # 首页
    url(r"/", index.IndexHandler, name="index"),
    # 爬虫模块
    url(r"/spiders", spiders.SpidersHandler, name="spiders"),
]
