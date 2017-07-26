# -*- coding:utf-8 -*-

import os

from tornado.web import url

from view import task
from view import index
from view import spiders
from view import monitor
from Websocket import task as ws_task
from Websocket import monitor as ws_monitor
from Utils.BaseHandle import ErrorHandler

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
    'default_handler_class': ErrorHandler,
    'default_handler_args': dict(status_code=404)
}

handlers = [
    # Index
    url(r"/", index.IndexHandler, name="index"),
    # Spider Modules
    url(r"/spiders", spiders.SpidersHandler, name="spiders"),
    # Spider Task
    url(r"/spider_task/(.+)", task.SpiderTaskHandler, name="spider_task"),
    # Monitor
    url(r"/monitor", monitor.MonitorHandler, name="monitor"),
    # Monitor Update Websocket
    (r"/update-monitor", ws_monitor.MonitorUpdateHandler),
    # Tasks Update Websocket
    (r"/update-tasks", ws_task.TasksUpdateHandler),
]
