# -*- utf-8 -*-

from .base_option import BaseOption
from Htmlrender.decorator import check_args
from Htmlrender.Cecharts.options.base_option import LineStyle3
from Htmlrender.Cecharts.options.base_option import Label3
from Htmlrender.Cecharts.options.base_option import ItemStyle
from Htmlrender.Cecharts.options.base_option import CheckPointStyle
from Htmlrender.Cecharts.options.base_option import ControlStyle
from Htmlrender.Cecharts.options.base_option import Data


__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class TimeLine(BaseOption):
    def __init__(self):
        self.show = None
        self.type = None
        self.axisType = None
        self.currentIndex = None
        self.autoPlay = None
        self.rewind = None
        self.loop = None
        self.playInterval = None
        self.realtime = None
        self.controlPosition = None
        self.zlevel = None
        self.z = None
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None
        self.padding = None
        self.orient = None
        self.inverse = None
        self.symbol = None
        self.symbolSize = None
        self.symbolRotate = None
        self.symbolOffset = None
        self.lineStyle = LineStyle3()
        self.label = Label3()
        self.itemStyle = ItemStyle()
        self.checkpointStyle = CheckPointStyle()
        self.controlStyle = ControlStyle()
        self.data = Data()

    @check_args
    def set_keys(self, show: bool=None, _type: str=None, axis_type: str=None, current_index: int=None,
                 auto_play: bool=None, rewind: bool=None, loop: bool=None, play_interval: int=None,
                 realtime: bool=None, control_position: str=None, z_level: int=None, z: int=None,
                 left=None, top=None, right=None, bottom=None, padding=None, orient: str=None,
                 inverse: bool=None, symbol: str=None, symbol_size=None, symbol_rotate: int=None,
                 symbol_offset: list=None):
        self.show = show
        self.type = _type
        self.axisType = axis_type
        self.currentIndex = current_index
        self.autoPlay = auto_play
        self.rewind = rewind
        self.loop = loop
        self.playInterval = play_interval
        self.realtime = realtime
        self.controlPosition = control_position
        self.zlevel = z_level
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.padding = padding
        self.orient = orient
        self.inverse = inverse
        self.symbol = symbol
        self.symbolSize = symbol_size
        self.symbolRotate = symbol_rotate
        self.symbolOffset = symbol_offset
