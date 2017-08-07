# -*- utf-8 -*-

from .base_option import BaseOption
from .text_style import TextStyle
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class AxisPointer(BaseOption):
    def __init__(self):
        self.type = None
        self.axis = None
        self.snap = None
        self.z = None
        self.label = None
        self.lineStyle = None
        self.shadowStyle = None
        self.crossStyle = None

    def set_keys(self, *args, **kwargs):
        pass
