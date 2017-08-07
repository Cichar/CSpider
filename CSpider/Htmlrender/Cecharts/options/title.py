# -*- utf-8 -*-

from .base_option import BaseOption
from .text_style import TextStyle
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class Title(BaseOption):
    @check_args
    def __init__(self, title: str=None, subtitle: str=None):
        self.show = None
        self.text = title
        self.link = None
        self.target = None
        self.textStyle = TextStyle()
        self.textAlign = None
        self.textBaseline = None
        self.subtext = subtitle
        self.sublink = None
        self.subtarget = None
        self.subtextStyle = TextStyle()
        self.padding = None
        self.itemGap = None
        self.zlevel = None
        self.z = None
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None
        self.backgroundColor = None
        self.borderColor = None
        self.borderWidth = None
        self.shadowBlur = None
        self.shadowColor = None
        self.shadowOffsetX = None
        self.shadowOffsetY = None

    @check_args
    def set_keys(self, show: bool=None, link: str=None, target: str=None, text_align: str=None,
                 text_base_line: str=None, sub_link: str=None, sub_target: str=None, padding: int=None,
                 item_gap: int=None, z_level: int=None, z: int=None, left=None, top=None, right=None,
                 bottom=None, background_color: str=None, border_color: str=None, border_width: int=None,
                 shadow_blur: int=None, shadow_color: str=None, shadow_offset_x: int=None,
                 shadow_offset_y: int=None):
        self.show = show
        self.link = link
        self.target = target
        self.textAlign = text_align
        self.textBaseline = text_base_line
        self.sublink = sub_link
        self.subtarget = sub_target
        self.padding = padding
        self.itemGap = item_gap
        self.zlevel = z_level
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.backgroundColor = background_color
        self.borderColor = border_color
        self.borderWidth = border_width
        self.shadowBlur = shadow_blur
        self.shadowColor = shadow_color
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y
