# -*- utf-8 -*-

from .base_option import BaseOption
from .text_style import TextStyle
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class Legend(BaseOption):
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
        self.orient = None
        self.align = None
        self.padding = None
        self.itemGap = None
        self.itemWidth = None
        self.itemHeight = None
        self.formatter = None
        self.selectedMode = None
        self.inactiveColor = None
        self.selected = None
        self.textStyle = TextStyle()
        self.tooltip = None
        self.data = []
        self.backgroundColor = None
        self.borderColor = None
        self.borderWidth = None
        self.shadowBlur = None
        self.shadowColor = None
        self.shadowOffsetX = None
        self.shadowOffsetY = None

    @check_args
    def set_keys(self, show: bool=None, z_level: int=None, z: int=None, left=None, top=None, right=None,
                 bottom=None, width=None, height=None, orient: str=None, align: str=None, padding: int=None,
                 item_gap: int=None, item_width: int=None, item_height: int=None, formatter=None,
                 selected_mode=None, inactive_color: str=None, selected: dict=None, data: list=None,
                 background_color: str=None, border_color: str=None, border_width: int=None,
                 shadow_blur: int=None, shadow_color: str=None, shadow_offset_x: int=None,
                 shadow_offset_y: int=None):
        self.show = show
        self.zlevel = z_level
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.width = width
        self.height = height
        self.orient = orient
        self.align = align
        self.padding = padding
        self.itemGap = item_gap
        self.itemWidth = item_width
        self.itemHeight = item_height
        self.formatter = formatter
        self.selectedMode = selected_mode
        self.inactiveColor = inactive_color
        self.selected = selected
        self.data = data
        self.backgroundColor = background_color
        self.borderColor = border_color
        self.borderWidth = border_width
        self.shadowBlur = shadow_blur
        self.shadowColor = shadow_color
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y
