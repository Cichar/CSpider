# -*- coding:utf-8 -*-

import os

from tornado.web import url

from view import index
from view import spiders
from view import task

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/6/27'
__Version__ = '0.1'

settings = {
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    'static_path': os.path.join(os.path.dirname(__file__), "static"),
    'debug': True,
    'xsrf_cookies': True,
    'cookie_secret': "aYCg6pESRtKos6GkHn/VB9oXbPT2g0R0kQvJ3/xJ89E=",
}

handlers = [
    # 首页
    url(r"/", index.IndexHandler, name="index"),
    # 爬虫模块
    url(r"/spiders", spiders.SpidersHandler, name="spiders"),
    # 添加爬虫任务
    url(r"/spider_task", task.SpiderTaskHandler, name="spider_task")
]
