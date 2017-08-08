# -*- utf-8 -*-

from .base_option import BaseOption
from .base_option import Name
from .base_option import AxisLine
from .base_option import AxisTick
from .base_option import AxisLabel
from .base_option import SplitLine
from .base_option import SplitArea
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class Radar(BaseOption):
    def __init__(self):
        self.zlevel = None
        self.z = None
        self.center = None
        self.radius = None
        self.startAngle = None
        self.name = Name()
        self.nameGap = None
        self.splitNumber = None
        self.shape = None
        self.scale = None
        self.silent = None
        self.triggerEvent = None
        self.axisLine = AxisLine()
        self.axisTick = AxisTick()
        self.axisLabel = AxisLabel()
        self.splitLine = SplitLine()
        self.splitArea = SplitArea()
        self.indicator = []

    @check_args
    def set_keys(self, z_level: int=None, z: int=None, center: list=None, radius=None, start_angle: int=None,
                 name_gap: int=None, split_num: int=None, shape: str=None, scale: bool=None, silent: bool=None,
                 trigger_event: bool=None, indicator: list=None):
        self.zlevel = z_level
        self.z = z
        self.center = center
        self.radius = radius
        self.startAngle = start_angle
        self.nameGap = name_gap
        self.splitNumber = split_num
        self.shape = shape
        self.scale = scale
        self.silent = silent
        self.triggerEvent = trigger_event
        self.indicator = indicator
