# -*- utf-8 -*-

from .base_option import BaseOption
from .base_option import TextStyle
from .axis_pointer import AxisPointer
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class Grid(BaseOption):
    def __init__(self):
        self.show = None
        self.zlevel = None
        self.z = None
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None
        self.width = None
        self.height = None
        self.containLabel = None
        self.backgroundColor = None
        self.borderColor = None
        self.borderWidth = None
        self.shadowBlur = None
        self.shadowColor = None
        self.shadowOffsetX = None
        self.shadowOffsetY = None
        self.tooltip = GToolTip()

    @check_args
    def set_keys(self, show: bool=None, z_level: int=None, z: int=None, left=None, top=None, right=None,
                 bottom=None, width=None, height=None, contain_label: bool=None, background_color: str=None,
                 border_color: str=None, border_width: int=None, shadow_blur: int=None, shadow_color: str=None,
                 shadow_offset_x: int=None, shadow_offset_y: int=None):
        self.show = show
        self.zlevel = z_level
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.width = width
        self.height = height
        self.containLabel = contain_label
        self.backgroundColor = background_color
        self.borderColor = border_color
        self.borderWidth = border_width
        self.shadowBlur = shadow_blur
        self.shadowColor = shadow_color
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y


class GToolTip(BaseOption):
    def __init__(self):
        self.show = None
        self.trigger = None
        self.axisPointer = AxisPointer()
        self.position = None
        self.formatter = None
        self.backgroundColor = None
        self.borderColor = None
        self.borderWidth = None
        self.padding = None
        self.textStyle = TextStyle()
        self.extraCssText = None

    @check_args
    def set_keys(self, show: bool=None, trigger: str=None, position=None, formatter=None,
                 background_color: str=None, border_color: str=None, border_width: str=None,
                 padding: int=None, extra_css_text: str=None):
        self.show = show
        self.trigger = trigger
        self.position = position
        self.formatter = formatter
        self.backgroundColor = background_color
        self.borderColor = border_color
        self.borderWidth = border_width
        self.padding = padding
        self.extraCssText = extra_css_text
