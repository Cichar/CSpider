# -*- utf-8 -*-

from .base_option import BaseOption
from Htmlrender.decorator import check_args
from Htmlrender.Cecharts.options.base_option import SplitLine
from Htmlrender.Cecharts.options.base_option import ItemStyle3
from Htmlrender.Cecharts.options.base_option import DayLabel
from Htmlrender.Cecharts.options.base_option import MonthLabel
from Htmlrender.Cecharts.options.base_option import YearLabel

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class Calendar(BaseOption):
    def __init__(self):
        self.zlevel = None
        self.z = None
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None
        self.width = None
        self.height = None
        self.range = None
        self.cellSize = None
        self.orient = None
        self.splitLine = SplitLine()
        self.itemStyle = ItemStyle3()
        self.dayLabel = DayLabel()
        self.monthLabel = MonthLabel()
        self.yearLabel = YearLabel()
        self.silent = None

    @check_args
    def set_keys(self, z_level: int=None, z: int=None, left=None, top=None, right=None, bottom=None,
                 width=None, height=None, _range=None, cell_size=None, orient: str=None, silent: bool=None):
        self.zlevel = z_level
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.width = width
        self.height = height
        self.range = _range
        self.cellSize = cell_size
        self.orient = orient
        self.silent = silent
