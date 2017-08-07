# -*- utf-8 -*-

from .base_option import BaseOption
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/6'
__Version__ = '0.1'


class TextStyle(BaseOption):
    def __init__(self):
        self.color = None
        self.fontStyle = None
        self.fontWeight = None
        self.fontFamily = None
        self.fontSize = None

    @check_args
    def set_keys(self, color: str=None, style: str=None, weight: str=None,
                 family: str=None, size: int=None):
        self.color = color
        self.fontStyle = style
        self.fontWeight = weight
        self.fontFamily = family
        self.fontSize = size
