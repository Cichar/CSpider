# -*- utf-8 -*-

from .base_option import BaseOption
from Htmlrender.Cecharts.options.base_option import Feature
from Htmlrender.Cecharts.options.base_option import IconStyle
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class ToolBox(BaseOption):
    """ This Class Is For Main ToolBox """

    def __init__(self):
        self.show = None
        self.orient = None
        self.itemSize = None
        self.itemGap = None
        self.showTitle = None
        self.feature = Feature()
        self.iconStyle = IconStyle()
        self.zlevel = None
        self.z = None
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None
        self.width = None
        self.height = None

    @check_args
    def set_keys(self, show: bool=None, orient: str=None, item_size: int=None, item_gap: int=None,
                 show_title: bool=None, z_level: int=None, z: int=None, left=None, top=None,
                 right=None, bottom=None, width=None, height=None):
        self.show = show
        self.orient = orient
        self.itemSize = item_size
        self.itemGap = item_gap
        self.showTitle = show_title
        self.zlevel = z_level
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.width = width
        self.height = height
