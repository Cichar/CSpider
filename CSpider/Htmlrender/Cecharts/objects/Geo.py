# -*- utf-8 -*-

from .base_object import BaseObject
from Htmlrender.Cecharts.options.base_option import ItemStyle2
from Htmlrender.Cecharts.options.base_option import Label2
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/9'
__Version__ = '0.1'


class Region(BaseObject):
    """ This Class Is For Geo.regions """

    def __init__(self):
        self.name = None
        self.selected = None
        self.itemStyle = ItemStyle2()
        self.label = Label2()

    @check_args
    def set_keys(self, name: str=None, selected: bool=None):
        self.name = name
        self.selected = selected
