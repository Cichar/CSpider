# -*- coding:utf-8 -*-

from tornado.options import define
from tornado.options import options

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/6/27'
__Version__ = '0.1'

"""
    Options For The Application
"""

define("port", default=8888, help="Run on the given port", type=int)

default_options = options
