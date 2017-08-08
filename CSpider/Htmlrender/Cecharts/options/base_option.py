# -*- utf-8 -*-

import abc
import json

from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class BaseOption(object):
    """ For Dict Option """

    @property
    def json(self):
        _json = {}
        for k, v in self.__dict__.items():
            if v:
                if hasattr(v, 'json'):
                    if v.json:
                        _json[k] = v.json
                else:
                    _json[k] = v
        return _json

    @abc.abstractmethod
    def set_keys(self, *args, **kwargs):
        pass

    def __str__(self):
        return json.dumps(self.json)


class BaseOption2(object):
    """ For Array Option """

    def __init__(self):
        self.__array = []

    @property
    def array(self):
        return self.__array

    @check_args
    def append(self, obj: object):
        if hasattr(obj, 'json'):
            self.__array.append(obj.json)
        elif isinstance(obj, dict):
            self.__array.append(obj)

    def __str__(self):
        return str(self.__array)


class TextStyle(BaseOption):
    def __init__(self):
        self.color = None
        self.fontStyle = None
        self.fontWeight = None
        self.fontFamily = None
        self.fontSize = None

    @check_args
    def set_keys(self, color: str=None, style: str=None, weight: str=None,
                 family: str=None, size: int=None):
        self.color = color
        self.fontStyle = style
        self.fontWeight = weight
        self.fontFamily = family
        self.fontSize = size


class TextStyle2(TextStyle):
    """ This Class Is For AxisLabel """

    def __init__(self):
        super().__init__()
        self.align = None
        self.baseline = None

    @check_args
    def set_keys(self, color: str=None, style: str=None, weight: str=None,
                 family: str=None, size: int=None, align: str=None, baseline: str=None):
        self.color = color
        self.fontStyle = style
        self.fontWeight = weight
        self.fontFamily = family
        self.fontSize = size
        self.align = align
        self.baseline = baseline


class Name(BaseOption):
    """ This Class Is For Radar """

    def __init__(self):
        self.show = None
        self.formatter = None
        self.textStyle = TextStyle()

    def set_keys(self, show: bool=None, formatter=None):
        self.show = show
        self.formatter = formatter


class DataBackground(BaseOption):
    def __init__(self):
        self.lineStyle = LineStyle()
        self.areaStyle = AreaStyle()

    def set_keys(self, *args, **kwargs):
        pass


class AreaStyle(BaseOption):
    def __init__(self):
        self.color = None
        self.shadowBlur = None
        self.shadowColor = None
        self.shadowOffsetX = None
        self.shadowOffsetY = None
        self.opacity = None

    @check_args
    def set_keys(self, color: list=None, shadow_blur: int=None, shadow_color: str=None,
                 shadow_offset_x: int=None, shadow_offset_y: int=None, opacity: int=None):
        self.color = color
        self.shadowBlur = shadow_blur
        self.shadowColor = shadow_color
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y
        self.opacity = opacity


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


class LineStyle2(LineStyle):
    """ This Class Is For SplitLine """

    @check_args
    def set_keys(self, color=None, width: int=None, _type: str=None, shadow_blur: int=None,
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


class AxisLine(BaseOption):
    """ This Class Is For RadiusAxis """

    def __init__(self):
        self.show = None
        self.lineStyle = LineStyle()

    @check_args
    def set_keys(self, show: bool=None):
        self.show = show


class AxisLine2(AxisLine):
    """ This Class Is For xAxis And yAxis """

    def __init__(self):
        super().__init__()
        self.onZero = None

    @check_args
    def set_keys(self, show: bool=None, on_zero: bool=None):
        self.show = show
        self.onZero = on_zero


class AxisTick(BaseOption):
    """ This Class Is For Radar """

    def __init__(self):
        self.show = None
        self.alignWithLabel = None
        self.inside = None
        self.length = None
        self.lineStyle = LineStyle()

    @check_args
    def set_keys(self, show: bool=None, align_with_label: bool=None, inside: bool=None,
                 length: int=None):
        self.show = show
        self.alignWithLabel = align_with_label
        self.inside = inside
        self.length = length


class AxisTick2(AxisTick):
    """ This Class Is For xAxis And yAxis """

    def __init__(self):
        super().__init__()
        self.interval = None

    @check_args
    def set_keys(self, show: bool=None, align_with_label: bool=None, interval=None, inside: bool=None,
                 length: int=None):
        self.show = show
        self.alignWithLabel = align_with_label
        self.interval = interval
        self.inside = inside
        self.length = length


class AxisLabel(BaseOption):
    """ This Class Is For Radar """

    def __init__(self):
        self.show = None
        self.inside = None
        self.rotate = None
        self.margin = None
        self.formatter = None
        self.showMinLabel = None
        self.showMaxLabel = None
        self.textStyle = TextStyle2()

    @check_args
    def set_keys(self, show: bool=None, inside: bool=None, rotate: int=None, margin: int=None,
                 formatter=None, show_min_label: bool=None, show_max_label: bool=None):
        self.show = show
        self.inside = inside
        self.rotate = rotate
        self.margin = margin
        self.formatter = formatter
        self.showMinLabel = show_min_label
        self.showMaxLabel = show_max_label


class AxisLabel2(AxisLabel):
    """ This Class Is For xAxis And yAxis """

    def __init__(self):
        super().__init__()
        self.interval = None

    @check_args
    def set_keys(self, show: bool=None, interval=None, inside: bool=None, rotate: int=None, margin: int=None,
                 formatter=None, show_min_label: bool=None, show_max_label: bool=None):
        self.show = show
        self.interval = interval
        self.inside = inside
        self.rotate = rotate
        self.margin = margin
        self.formatter = formatter
        self.showMinLabel = show_min_label
        self.showMaxLabel = show_max_label


class SplitLine(BaseOption):
    """ This Class Is For Radar """

    def __init__(self):
        self.show = None
        self.lineStyle = LineStyle2()

    @check_args
    def set_keys(self, show: bool=None):
        self.show = show


class SplitLine2(SplitLine):
    """ This Class Is For xAxis And yAxis """

    def __init__(self):
        super().__init__()
        self.interval = None

    @check_args
    def set_keys(self, show: bool=None, interval=None):
        self.show = show
        self.interval = interval


class SplitArea(BaseOption):
    """ This Class Is For Radar """

    def __init__(self):
        self.show = None
        self.areaStyle = AreaStyle()

    @check_args
    def set_keys(self, show: bool=None):
        self.show = show


class SplitArea2(SplitArea):
    """ This Class Is For xAxis And yAxis """

    def __init__(self):
        super().__init__()
        self.interval = None

    @check_args
    def set_keys(self, show: bool=None, interval=None):
        self.show = show
        self.interval = interval


class Handle(BaseOption):
    def __init__(self):
        self.show = None
        self.icon = None
        self.size = None
        self.margin = None
        self.color = None
        self.throttle = None
        self.shadowBlur = None
        self.shadowColor = None
        self.shadowOffsetX = None
        self.shadowOffsetY = None

    def set_keys(self, show: bool=None, icon: str=None, size=None, margin: int=None, color: str=None,
                 throttle: int=None, shadow_blur: int=None, shadow_color: str=None, shadow_offset_x: int=None,
                 shadow_offset_y: int=None):
        self.show = show
        self.icon = icon
        self.size = size
        self.margin = margin
        self.color = color
        self.throttle = throttle
        self.shadowBlur = shadow_blur
        self.shadowColor = shadow_color
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y


class HandleStyle(BaseOption):
    def __init__(self):
        self.color = None
        self.borderColor = None
        self.borderWidth = None
        self.borderType = None
        self.shadowBlur = None
        self.shadowColor = None
        self.shadowOffsetX = None
        self.shadowOffsetY = None
        self.opacity = None

    def set_keys(self, color: str=None, border_color: str=None, border_width: int=None, border_type: str=None,
                 shadow_blur: int=None, shadow_color: str=None, shadow_offset_x: int=None, shadow_offset_y: int=None,
                 opacity: int=None):
        self.color = color
        self.borderColor = border_color
        self.borderWidth = border_width
        self.borderType = border_type
        self.shadowBlur = shadow_blur
        self.shadowColor = shadow_color
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y
        self.opacity = opacity
