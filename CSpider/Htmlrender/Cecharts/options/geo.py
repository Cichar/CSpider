# -*- utf-8 -*-

from .base_option import BaseOption
from Htmlrender.Cecharts.options.base_option import ScaleLimit
from Htmlrender.Cecharts.options.base_option import Label2
from Htmlrender.Cecharts.options.base_option import ItemStyle
from Htmlrender.Cecharts.options.base_option import Regions
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class Geo(BaseOption):
    def __init__(self):
        self.show = None
        self.map = None
        self.roam = None
        self.center = None
        self.aspectScale = None
        self.boundingCoords = None
        self.zoom = None
        self.scaleLimit = ScaleLimit()
        self.nameMap = None
        self.selectedMode = None
        self.label = Label2()
        self.itemStyle = ItemStyle()
        self.zlevel = None
        self.z = None
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None
        self.layoutCenter = None
        self.layoutSize = None
        self.regions = Regions()
        self.silent = None

    @check_args
    def set_keys(self, show: bool=None, _map: str=None, roam: bool=None, center: list=None,
                 aspect_scale: int=None, bounding_coords: list=None, zoom: int=None, name_map: dict=None,
                 selected_mode=None, z_level: int=None, z: int=None, left=None, top=None, right=None, bottom=None,
                 layout_center: list=None, layout_size=None, silent: bool=None):
        self.show = show
        self.map = _map
        self.roam = roam
        self.center = center
        self.aspectScale = aspect_scale
        self.boundingCoords = bounding_coords
        self.zoom = zoom
        self.nameMap = name_map
        self.selectedMode = selected_mode
        self.zlevel = z_level
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.layoutCenter = layout_center
        self.layoutSize = layout_size
        self.silent = silent
