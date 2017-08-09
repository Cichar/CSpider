# -*- utf-8 -*-

from .base_option import BaseOption
from Htmlrender.Cecharts.options.base_option import InBrush
from Htmlrender.Cecharts.options.base_option import OutOfBrush
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class Brush(BaseOption):
    def __init__(self):
        self.toolbox = None
        self.brushLink = None
        self.seriesIndex = None
        self.geoIndex = None
        self.xAxisIndex = None
        self.yAxisIndex = None
        self.brushType = None
        self.brushMode = None
        self.transformable = None
        self.brushStyle = None
        self.throttleType = None
        self.throttleDelay = None
        self.removeOnClick = None
        self.inBrush = InBrush()
        self.outOfBrush = OutOfBrush()
        self.z = None

    @check_args
    def set_keys(self, toolbox: list=None, brush_link=None, series_index=None, geo_index=None, x_axis_index=None,
                 y_axis_index=None, brush_type: str =None, brush_mode: str=None, transformable: bool=None,
                 brush_style: dict=None, throttle_type: str=None, throttle_delay: int=None, remove_on_click: int=None,
                 z: int=None):
        self.toolbox = toolbox
        self.brushLink = brush_link
        self.seriesIndex = series_index
        self.geoIndex = geo_index
        self.xAxisIndex = x_axis_index
        self.yAxisIndex = y_axis_index
        self.brushType = brush_type
        self.brushMode = brush_mode
        self.transformable = transformable
        self.brushStyle = brush_style
        self.throttleType = throttle_type
        self.throttleDelay = throttle_delay
        self.removeOnClick = remove_on_click
        self.z = z
