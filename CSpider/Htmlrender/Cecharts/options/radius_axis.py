# -*- utf-8 -*-

from .base_option import BaseOption
from .base_option import TextStyle
from .base_option import AxisLine
from .base_option import AxisTick2
from .base_option import AxisLabel2
from .base_option import SplitLine2
from .base_option import SplitArea2
from .axis_pointer import AxisPointer2
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class RadiusAxis(BaseOption):
    def __init__(self):
        self.polarIndex = None
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
        self.data = []
        self.axisPointer = AxisPointer2()
        self.zlevel = None
        self.z = None

    @check_args
    def set_keys(self, polar_index: int=None, _type: str=None, name: str=None, name_location: str=None, name_gap: int=None,
                 name_rotate: int=None, inverse: bool=None, boundary_gap=None, _min=None, _max=None, scale: bool=None,
                 split_num: int=None, min_interval: int=None, interval: int=None, log_base: int=None, silent: bool=None,
                 trigger_event: bool=None, data: list=None, z_level: int=None, z: int=None):
        self.polarIndex = polar_index
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
        self.data = data
        self.zlevel = z_level
        self.z = z