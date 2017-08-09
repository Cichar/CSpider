# -*- utf-8 -*-

from Htmlrender.Cecharts.options.base_option import ParallelAxisDefault
from Htmlrender.Cecharts.options.base_option import AreaSelectStyle
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class ParallelAxis(ParallelAxisDefault):
    def __init__(self):
        super().__init__()
        self.dim = None
        self.parallelIndex = None
        self.realtime = None
        self.areaSelectStyle = AreaSelectStyle()

    @check_args
    def set_keys(self, dim: int=None, parallel_index: int=None, realtime: bool=None, _type: str=None,
                 name: str=None, name_location: str=None, name_gap: int=None, name_rotate: int=None,
                 inverse: bool=None, boundary_gap=None, _min=None, _max=None, scale: bool=None,
                 split_num: int=None, min_interval: int=None, interval: int=None, log_base: int=None,
                 silent: bool=None, trigger_event: bool=None):
        self.dim = dim
        self.parallelIndex = parallel_index
        self.realtime = realtime
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
