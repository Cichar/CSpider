# -*- utf-8 -*-

from .base_option import BaseOption
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class Geo(BaseOption):
    @check_args
    def set_keys(self, *args, **kwargs):
        pass