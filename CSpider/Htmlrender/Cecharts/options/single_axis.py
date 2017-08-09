# -*- utf-8 -*-

from .base_option import BaseOption
from Htmlrender.decorator import check_args
from Htmlrender.Cecharts.options.base_option import TextStyle
from Htmlrender.Cecharts.options.base_option import AxisLine
from Htmlrender.Cecharts.options.base_option import AxisTick2
from Htmlrender.Cecharts.options.base_option import AxisLabel2
from Htmlrender.Cecharts.options.base_option import SplitLine2
from Htmlrender.Cecharts.options.base_option import SplitArea2
from Htmlrender.Cecharts.options.base_option import Data
from Htmlrender.Cecharts.options.axis_pointer import AxisPointer2
from Htmlrender.Cecharts.options.tooltip import ToolTip

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class SingleAxis(BaseOption):
    def __init__(self):
        self.zlevel = None
        self.z = None
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None
        self.width = None
        self.height = None
        self.orient = None
        self.type = None
        self.name = None
        self.nameLocation = None
        self.nameTextStyle = TextStyle()
        self.nameGap = None
        self.nameRotate = None
        self.inverse = None
        self.boundaryGap = None
        self.min = None
        self.max = None
        self.scale = None
        self.splitNumber = None
        self.minInterval = None
        self.interval = None
        self.logBase = None
        self.silent = None
        self.triggerEvent = None
        self.axisLine = AxisLine()
        self.axisTick = AxisTick2()
        self.axisLabel = AxisLabel2()
        self.splitLine = SplitLine2()
        self.splitArea = SplitArea2()
        self.data = Data()
        self.axisPointer = AxisPointer2()
        self.tooltip = ToolTip()

    @check_args
    def set_keys(self, z_level: int=None, z: int=None, left=None, top=None, right=None, bottom=None,
                 width=None, height=None, orient: str=None, _type: str=None, name: str=None,
                 name_location: str=None, name_gap: int=None, name_rotate: int=None, inverse: bool=None,
                 boundary_gap=None, _min=None, _max=None, scale: bool=None, split_num: int=None,
                 min_interval: int=None, interval: int=None, log_base: int=None, silent: bool=None,
                 trigger_event: bool=None):
        self.zlevel = z_level
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.width = width
        self.height = height
        self.orient = orient
        self.type = _type
        self.name = name
        self.nameLocation = name_location
        self.nameGap = name_gap
        self.nameRotate = name_rotate
        self.inverse = inverse
        self.boundaryGap = boundary_gap
        self.min = _min
        self.max = _max
        self.scale = scale
        self.splitNumber = split_num
        self.minInterval = min_interval
        self.interval = interval
        self.logBase = log_base
        self.silent = silent
        self.triggerEvent = trigger_event
