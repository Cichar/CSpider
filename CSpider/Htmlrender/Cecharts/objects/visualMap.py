# -*- utf-8 -*-

from .base_object import BaseObject
from Htmlrender.Cecharts.options.base_option import TextStyle
from Htmlrender.Cecharts.options.base_option import Controller
from Htmlrender.Cecharts.options.base_option import InRange
from Htmlrender.Cecharts.options.base_option import OutOfRange
from Htmlrender.decorator import check_args


__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/9'
__Version__ = '0.1'


class Continuous(BaseObject):
    def __init__(self):
        self.type = 'continuous'
        self.min = None
        self.max = None
        self.range = None
        self.calculable = None
        self.realtime = None
        self.inverse = None
        self.precision = None
        self.itemWidth = None
        self.itemHeight = None
        self.align = None
        self.text = None
        self.textGap = None
        self.show = None
        self.dimension = None
        self.seriesIndex = None
        self.hoverLink = None
        self.inRange = InRange()
        self.outOfRange = OutOfRange()
        self.controller = Controller()
        self.zlevel = None
        self.z = None
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None
        self.orient = None
        self.padding = None
        self.backgroundColor = None
        self.borderColor = None
        self.borderWidth = None
        self.color = None
        self.textStyle = TextStyle()
        self.formatter = None

    @check_args
    def set_keys(self, _min: int=None, _max: int=None, _range: list=None, calculabel: bool=None, realtime: bool=None,
                 inverse: bool=None, precision: int=None, item_width: int=None, item_height: int=None, align: str=None,
                 text: list=None, text_gap: list=None, show: bool=None, dimension: int=None, series_index=None,
                 hover_link: bool=None, z_level: int=None, z: int=None, left=None, top=None, right=None, bottom=None,
                 orient: str=None, padding=None, background_color: str=None, border_color: str=None,
                 border_width: int=None, color: list=None, formatter=None):
        self.min = _min
        self.max = _max
        self.range = _range
        self.calculable = calculabel
        self.realtime = realtime
        self.inverse = inverse
        self.precision = precision
        self.itemWidth = item_width
        self.itemHeight = item_height
        self.align = align
        self.text = text
        self.textGap = text_gap
        self.show = show
        self.dimension = dimension
        self.seriesIndex = series_index
        self.hoverLink = hover_link
        self.zlevel = z_level
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.orient = orient
        self.padding = padding
        self.backgroundColor = background_color
        self.borderColor = border_color
        self.borderWidth = border_width
        self.color = color
        self.formatter = formatter


class Piecewise(BaseObject):
    def __init__(self):
        self.type = 'piecewise'
        self.splitNumber = None
        self.pieces = None
        self.categories = None
        self.min = None
        self.max = None
        self.minOpen = None
        self.maxOpen = None
        self.selectedMode = None
        self.inverse = None
        self.precision = None
        self.itemWidth = None
        self.itemHeight = None
        self.align = None
        self.text = None
        self.textGap = None
        self.showLabel = None
        self.itemGap = None
        self.itemSymbol = None
        self.show = None
        self.dimension = None
        self.seriesIndex = None
        self.hoverLink = None
        self.inRange = InRange()
        self.outOfRange = OutOfRange()
        self.controller = Controller()
        self.zlevel = None
        self.z = None
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None
        self.orient = None
        self.padding = None
        self.backgroundColor = None
        self.borderColor = None
        self.borderWidth = None
        self.color = None
        self.textStyle = TextStyle()
        self.formatter = None

    @check_args
    def set_keys(self, split_num: int=None, pieces: list=None, categories: list=None, _min: int = None,
                 _max: int = None, min_open: bool=None, max_open: bool=None, selected_mode: str=None,
                 inverse: bool = None, precision: int = None, item_width: int = None, item_height: int = None,
                 align: str = None, text: list = None, text_gap: list = None, show_label: bool=None, item_gap: int=None,
                 item_symbol: str=None, show: bool = None, dimension: int = None, series_index=None,
                 hover_link: bool = None, z_level: int = None, z: int = None, left=None, top=None, right=None,
                 bottom=None, orient: str = None, padding=None, background_color: str = None, border_color: str = None,
                 border_width: int = None, color: list = None, formatter=None):
        self.splitNumber = split_num
        self.pieces = pieces
        self.categories = categories
        self.min = _min
        self.max = _max
        self.minOpen = min_open
        self.maxOpen = max_open
        self.selectedMode = selected_mode
        self.inverse = inverse
        self.precision = precision
        self.itemWidth = item_width
        self.itemHeight = item_height
        self.align = align
        self.text = text
        self.textGap = text_gap
        self.showLabel = show_label
        self.itemGap = item_gap
        self.itemSymbol = item_symbol
        self.show = show
        self.dimension = dimension
        self.seriesIndex = series_index
        self.hoverLink = hover_link
        self.zlevel = z_level
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.orient = orient
        self.padding = padding
        self.backgroundColor = background_color
        self.borderColor = border_color
        self.borderWidth = border_width
        self.color = color
        self.formatter = formatter
