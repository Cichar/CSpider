# -*- utf-8 -*-

from .base_object import BaseObject
from Htmlrender.Cecharts.options.base_option import TextStyle
from Htmlrender.Cecharts.options.base_option import HandleStyle
from Htmlrender.Cecharts.options.base_option import DataBackground
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class Inside(BaseObject):
    def __init__(self):
        self.type = 'inside'
        self.disabled = None
        self.xAxisIndex = None
        self.yAxisIndex = None
        self.radiusAxisIndex = None
        self.angleAxisIndex = None
        self.filterMode = None
        self.start = None
        self.end = None
        self.startValue = None
        self.endValue = None
        self.minSpan = None
        self.maxSpan = None
        self.minValueSpan = None
        self.maxValueSpan = None
        self.orient = None
        self.zoomLock = None
        self.throttle = None
        self.zoomOnMouseWheel = None
        self.moveOnMouseMove = None
        self.preventDefaultMouseMove = None

    @check_args
    def set_keys(self, disabled: bool=None, x_axis_index=None, y_axis_index=None, radius_axis_index=None,
                 angle_axis_index=None, filter_mode: str=None, start: int=None, end: int=None, start_value=None,
                 end_value=None, min_span: int=None, max_span: int=None, min_value_span=None, max_value_span=None,
                 orient: str=None, zoomlock: bool=None, throttle: int=None, zoom_on_mouse_wheel: bool=None,
                 move_on_mouse_move: bool=None, prevent_default_mouse_move: bool=None):
        self.disabled = disabled
        self.xAxisIndex = x_axis_index
        self.yAxisIndex = y_axis_index
        self.radiusAxisIndex = radius_axis_index
        self.angleAxisIndex = angle_axis_index
        self.filterMode = filter_mode
        self.start = start
        self.end = end
        self.startValue = start_value
        self.endValue = end_value
        self.minSpan = min_span
        self.maxSpan = max_span
        self.minValueSpan = min_value_span
        self.maxValueSpan = max_value_span
        self.orient = orient
        self.zoomLock = zoomlock
        self.throttle = throttle
        self.zoomOnMouseWheel = zoom_on_mouse_wheel
        self.moveOnMouseMove = move_on_mouse_move
        self.preventDefaultMouseMove = prevent_default_mouse_move


class Slider(BaseObject):
    def __init__(self):
        self.type = 'slider'
        self.show = None
        self.backgroundColor = None
        self.dataBackground = DataBackground()
        self.fillerColor = None
        self.borderColor = None
        self.handleIcon = None
        self.handleSize = None
        self.handleStyle = HandleStyle()
        self.labelPrecision = None
        self.labelFormatter = None
        self.showDetail = None
        self.showDataShadow = None
        self.realtime = None
        self.textStyle = TextStyle()
        self.xAxisIndex = None
        self.yAxisIndex = None
        self.radiusAxisIndex = None
        self.angleAxisIndex = None
        self.filterMode = None
        self.start = None
        self.end = None
        self.startValue = None
        self.endValue = None
        self.minSpan = None
        self.maxSpan = None
        self.minValueSpan = None
        self.maxValueSpan = None
        self.orient = None
        self.zoomLock = None
        self.throttle = None
        self.zlevel = None
        self.z = None
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None

    @check_args
    def set_keys(self, show: bool=None, background_color: str=None, filler_color: str=None, border_color: str=None,
                 handle_icon: str=None, handle_size: str=None, label_precision: int=None, label_formatter=None,
                 show_detail: bool=None, show_data_shadow: str=None, realtime: bool=None, x_axis_index=None,
                 y_axis_index=None, radius_axis_index=None, angle_axis_index=None, filter_mode: str=None,
                 start: int=None, end: int=None, start_value=None, end_value=None, min_span: int=None,
                 max_span: int=None, min_value_span=None, max_value_span=None, orient: str=None, zoomlock: bool=None,
                 throttle: int=None, z_level: int=None, z: int=None, left=None, top=None, right=None, bottom=None):
        self.show = show
        self.backgroundColor = background_color
        self.fillerColor = filler_color
        self.borderColor = border_color
        self.handleIcon = handle_icon
        self.handleSize = handle_size
        self.labelPrecision = label_precision
        self.labelFormatter = label_formatter
        self.showDetail = show_detail
        self.showDataShadow = show_data_shadow
        self.realtime = realtime
        self.xAxisIndex = x_axis_index
        self.yAxisIndex = y_axis_index
        self.radiusAxisIndex = radius_axis_index
        self.angleAxisIndex = angle_axis_index
        self.filterMode = filter_mode
        self.start = start
        self.end = end
        self.startValue = start_value
        self.endValue = end_value
        self.minSpan = min_span
        self.maxSpan = max_span
        self.minValueSpan = min_value_span
        self.maxValueSpan = max_value_span
        self.orient = orient
        self.zoomLock = zoomlock
        self.throttle = throttle
        self.zlevel = z_level
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
