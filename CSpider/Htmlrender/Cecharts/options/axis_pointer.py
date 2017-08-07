# -*- utf-8 -*-

from .base_option import BaseOption
from .base_option import TextStyle
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class AxisPointer(BaseOption):
    def __init__(self):
        self.type = None
        self.axis = None
        self.snap = None
        self.z = None
        self.label = Label()
        self.lineStyle = LineStyle()
        self.shadowStyle = ShadowStyle()
        self.crossStyle = CrossStyle()

    @check_args
    def set_keys(self, _type: str=None, axis: str=None, snap: bool=None, z: int=None):
        self.type = _type
        self.axis = axis
        self.snap = snap
        self.z = z


class Label(BaseOption):
    def __init__(self):
        self.show = None
        self.precision = None
        self.formatter = None
        self.margin = None
        self.textStyle = TextStyle()
        self.padding = None
        self.backgroundColor = None
        self.borderColor = None
        self.borderWidth = None
        self.shadowBlur = None
        self.shadowColor = None
        self.shadowOffsetX = None
        self.shadowOffsetY = None

    @check_args
    def set_keys(self, show: bool=None, precision=None, formatter=None, margin: int=None, padding=None,
                 background_color: str=None, border_color: str=None, border_width: str=None, shadow_blur: int=None,
                 shadow_color: str=None, shadow_offset_x: int=None, shadow_offset_y: int=None):
        self.show = show
        self.precision = precision
        self.formatter = formatter
        self.margin = margin
        self.padding = padding
        self.backgroundColor = background_color
        self.borderColor = border_color
        self.borderWidth = border_width
        self.shadowBlur = shadow_blur
        self.shadowColor = shadow_color
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y


class LineStyle(BaseOption):
    def __init__(self):
        self.color = None
        self.width = None
        self.type = None
        self.shadowBlur = None
        self.shadowColor = None
        self.shadowOffsetX = None
        self.shadowOffsetY = None
        self.opacity = None

    @check_args
    def set_keys(self, color: str=None, width: int=None, _type: str=None, shadow_blur: int=None,
                 shadow_color: str=None, shadow_offset_x: int=None, shadow_offset_y: int=None, opacity: int=None):
        self.color = color
        self.width = width
        self.type = _type
        self.shadowBlur = shadow_blur
        self.shadowColor = shadow_color
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y
        self.opacity = opacity


class ShadowStyle(BaseOption):
    def __init__(self):
        self.color = None
        self.shadowBlur = None
        self.shadowColor = None
        self.shadowOffsetX = None
        self.shadowOffsetY = None
        self.opacity = None

    @check_args
    def set_keys(self, color: str=None, shadow_blur: int=None, shadow_color: str=None, shadow_offset_x: int=None,
                 shadow_offset_y: int=None, opacity: int=None):
        self.color = color
        self.shadowBlur = shadow_blur
        self.shadowColor = shadow_color
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y
        self.opacity = opacity


class CrossStyle(BaseOption):
    def __init__(self):
        self.color = None
        self.width = None
        self.type = None
        self.shadowBlur = None
        self.shadowColor = None
        self.shadowOffsetX = None
        self.shadowOffsetY = None
        self.opacity = None

    @check_args
    def set_keys(self, color: str=None, width: int=None, _type: str=None, shadow_blur: int=None,
                 shadow_color: str=None, shadow_offset_x: int=None, shadow_offset_y: int=None, opacity: int=None):
        self.color = color
        self.width = width
        self.type = _type
        self.shadowBlur = shadow_blur
        self.shadowColor = shadow_color
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y
        self.opacity = opacity
