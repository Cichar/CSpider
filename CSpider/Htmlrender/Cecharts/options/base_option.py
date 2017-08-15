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
                elif hasattr(v, 'array'):
                    if v.array:
                        _json[k] = v.array
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
    def append(self, *objects: object):
        for obj in objects:
            if hasattr(obj, 'json'):
                self.__array.append(obj.json)
            elif isinstance(obj, dict):
                self.__array.append(obj)
            elif isinstance(obj, list):
                for _ in obj:
                    self.__array.append(_)

    def __str__(self):
        return str(self.__array)


class Data(BaseOption2):
    pass


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


class Label2(BaseOption):
    """ This Class Is For Geo """

    def __init__(self):
        self.normal = Normal2()
        self.emphasis = Emphasis2()

    @check_args
    def set_keys(self, *args, **kwargs):
        pass


class Label3(BaseOption):
    """ This Class Is For Timeline """

    def __init__(self):
        self.normal = Normal4()
        self.emphasis = Emphasis4()

    def set_keys(self, *args, **kwargs):
        pass


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


class LineStyle3(LineStyle):
    """ This Class Is For Timeline """

    def __init__(self):
        super().__init__()
        self.show = None

    @check_args
    def set_keys(self, show: bool=None, color: str = None, width: int = None, _type: str = None,
                 shadow_blur: int = None, shadow_color: str = None, shadow_offset_x: int = None,
                 shadow_offset_y: int = None, opacity: int = None):
        self.show = show
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


class Controller(BaseOption):
    """ This Class Is For VisualMap Object """
    def __init__(self):
        self.inRange = InRange()
        self.outOfRange = OutOfRange()

    def set_keys(self, *args, **kwargs):
        pass


class InRange(BaseOption):
    """ This Class Is For Controller """

    def __init__(self):
        self.symbol = None
        self.symbolSize = None
        self.color = None
        self.colorAlpha = None
        self.opacity = None
        self.colorLightness = None
        self.colorSaturation = None
        self.colorHue = None

    @check_args
    def set_keys(self, symbol: list=None, symbol_size: list=None, color: list=None, color_alpha: list=None,
                 opacity: list=None, color_lightness: list=None, color_saturation: list=None, color_hue: list=None):
        self.symbol = symbol
        self.symbolSize = symbol_size
        self.color = color
        self.colorAlpha = color_alpha
        self.opacity = opacity
        self.colorLightness = color_lightness
        self.colorSaturation = color_saturation
        self.colorHue = color_hue


class OutOfRange(InRange):
    """ This Class Is For Controller """
    pass


class InBrush(InRange):
    """ This Class Is For Brush """


class OutOfBrush(InRange):
    """ This Class Is For Brush """


class Feature(BaseOption):
    """ This Class Is For ToolBox """

    def __init__(self):
        self.saveAsImage = SaveAsImage()
        self.restore = Restore()
        self.dataView = DataView()
        self.dataZoom = DataZoom()
        self.magicType = MagicType()
        self.brush = Brush()

    @check_args
    def set_keys(self, *args, **kwargs):
        pass


class SaveAsImage(BaseOption):
    """ This Class Is For Feature """

    def __init__(self):
        self.type = None
        self.name = None
        self.backgroundColor = None
        self.excludeComponents = None
        self.show = None
        self.title = None
        self.icon = None
        self.iconStyle = IconStyle()
        self.pixelRatio = None

    @check_args
    def set_keys(self, _type: str=None, name: str=None, background_color: str=None, exclude_components: list=None,
                 show: bool=None, title: str=None, icon=None, pixel_ratio: int=None):
        self.type = _type
        self.name = name
        self.backgroundColor = background_color
        self.excludeComponents = exclude_components
        self.show = show
        self.title = title
        self.icon = icon
        self.pixelRatio = pixel_ratio


class Restore(BaseOption):
    """ This Class Is For Feature """

    def __init__(self):
        self.show = None
        self.title = None
        self.icon = None
        self.iconStyle = IconStyle()

    @check_args
    def set_keys(self, show: bool=None, title: str=None, icon=None):
        self.show = show
        self.title = title
        self.icon = icon


class DataView(BaseOption):
    """ This Class Is For Feature """

    def __init__(self):
        self.show = None
        self.title = None
        self.icon = None
        self.iconStyle = IconStyle()
        self.readOnly = None
        self.optionToContent = None
        self.contentToOption = None
        self.lang = None
        self.backgroundColor = None
        self.textareaColor = None
        self.textareaBorderColor = None
        self.textColor = None
        self.buttonColor = None
        self.buttonTextColor = None

    @check_args
    def set_keys(self, show: bool=None, title: str=None, icon=None, read_only: bool=None, option_2_content=None,
                 content_2_option=None, lang: list=None, background_color: str=None, text_area_color: str=None,
                 text_area_border_color: str=None, text_color: str=None, button_color: str=None,
                 button_text_color: str=None):
        self.show = show
        self.title = title
        self.icon = icon
        self.readOnly = read_only
        self.optionToContent = option_2_content
        self.contentToOption = content_2_option
        self.lang = lang
        self.backgroundColor = background_color
        self.textareaColor = text_area_color
        self.textareaBorderColor = text_area_border_color
        self.textColor = text_color
        self.buttonColor = button_color
        self.buttonTextColor = button_text_color


class DataZoom(BaseOption):
    """ This Class Is For Feature """

    def __init__(self):
        self.show = None
        self.title = Title()
        self.icon = Icon()
        self.iconStyle = IconStyle()
        self.xAxisIndex = None
        self.yAxisIndex = None

    @check_args
    def set_keys(self, show: bool=None, x_axis_index=None, y_axis_index=None):
        self.show = show
        self.xAxisIndex = x_axis_index
        self.yAxisIndex = y_axis_index


class Title(BaseOption):
    """ This Class Is For DataZoom """

    def __init__(self):
        self.zoom = None
        self.back = None

    @check_args
    def set_keys(self, zoom: str=None, back: str=None):
        self.zoom = zoom
        self.back = back


class Title2(BaseOption):
    """ This Class Is For MagicType """

    def __init__(self):
        self.line = None
        self.bar = None
        self.stack = None
        self.tiled = None

    @check_args
    def set_keys(self, line: str=None, bar: str=None, stack: str=None, tiled: str=None):
        self.line = line
        self.bar = bar
        self.stack = stack
        self.tiled = tiled


class Title3(BaseOption):
    """ This Class Is For Brush """

    def __init__(self):
        self.rect = None
        self.polygon = None
        self.lineX = None
        self.lineY = None
        self.keep = None
        self.clear = None

    @check_args
    def set_keys(self, rect: str=None, polygon: str=None, line_x: str=None, line_y: str=None,
                 keep: str=None, clear: str=None):
        self.rect = rect
        self.polygon = polygon
        self.lineX = line_x
        self.lineY = line_y
        self.keep = keep
        self.clear = clear


class Icon(Title):
    """ This Class Is For DataZoom """
    pass


class Icon2(Title2):
    """ This Class Is For MagicType """
    pass


class Icon3(Title3):
    """ This Class Is For Brush """
    pass


class MagicType(BaseOption):
    """ This Class Is For Feature 
        option and seriesIndex is not need to change,
        so this class not provide option and seriesIndex.
    """

    def __init__(self):
        self.show = None
        self.type = None
        self.title = Title2()
        self.icon = Icon2()
        self.iconStyle = IconStyle()

    @check_args
    def set_keys(self, show: bool=None, _type: list=None):
        self.show = show
        self.type = _type


class Brush(BaseOption):
    """ This Class Is For Feature """

    def __init__(self):
        self.type = None
        self.icon = Icon3()
        self.title = Title3()

    @check_args
    def set_keys(self, _type: list=None):
        self.type = _type


class IconStyle(BaseOption):
    """ This Class Is For ToolBox """

    def __init__(self):
        self.normal = Normal()
        self.emphasis = Emphasis()

    def set_keys(self, *args, **kwargs):
        pass


class ItemStyle(BaseOption):
    """ This Class Is For Geo """

    def __init__(self):
        self.normal = Emphasis()
        self.emphasis = Emphasis()

    def set_keys(self, *args, **kwargs):
        pass


class ItemStyle2(BaseOption):
    """ This Class Is For Region Object """

    def __init__(self):
        self.normal = Normal3()
        self.emphasis = Emphasis3()

    def set_keys(self, *args, **kwargs):
        pass


class Emphasis(BaseOption):
    """ This Class Is For IconStyle """

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

    @check_args
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


class Emphasis2(BaseOption):
    """ This Class Is For Label2 """

    def __init__(self):
        self.show = None
        self.textStyle = TextStyle()

    @check_args
    def set_keys(self, show: bool=None):
        self.show = show


class Emphasis3(Emphasis):
    """ This Class Is For Region Object """

    def __init__(self):
        super().__init__()
        self.areaColor = None

    @check_args
    def set_keys(self, area_color: str=None, color: str=None, border_color: str=None, border_width: int=None,
                 border_type: str=None, shadow_blur: int=None, shadow_color: str=None, shadow_offset_x: int=None,
                 shadow_offset_y: int=None, opacity: int=None):
        self.color = color
        self.borderColor = border_color
        self.borderWidth = border_width
        self.borderType = border_type
        self.shadowBlur = shadow_blur
        self.shadowColor = shadow_color
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y
        self.opacity = opacity
        self.areaColor = area_color


class Emphasis4(BaseOption):
    """ This Class Is For Label3 """

    def __init__(self):
        self.show = None
        self.interval = None
        self.rotate = None
        self.formatter = None
        self.textStyle = TextStyle2()

    @check_args
    def set_keys(self, show: bool=None, interval=None, rotate=None, formatter=None):
        self.show = show
        self.interval = interval
        self.rotate = rotate
        self.formatter = formatter


class Emphasis5(BaseOption):
    """ This Class Is For ControlStyle """

    def __init__(self):
        self.color = None
        self.borderColor = None
        self.borderWidth = None

    @check_args
    def set_keys(self, color: str=None, border_color: str=None, border_width: int=None):
        self.color = color
        self.borderColor = border_color
        self.borderWidth = border_width


class Normal(Emphasis):
    """ This Class Is For IconStyle """

    def __init__(self):
        super().__init__()
        self.textPosition = None
        self.textAlign = None

    @check_args
    def set_keys(self, color: str = None, border_color: str = None, border_width: int = None, border_type: str = None,
                 shadow_blur: int = None, shadow_color: str = None, shadow_offset_x: int = None,
                 shadow_offset_y: int = None, opacity: int = None, text_position: str=None, text_align: str=None):
        self.color = color
        self.borderColor = border_color
        self.borderWidth = border_width
        self.borderType = border_type
        self.shadowBlur = shadow_blur
        self.shadowColor = shadow_color
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y
        self.opacity = opacity
        self.textPosition = text_position
        self.textAlign = text_align


class Normal2(Emphasis2):
    """ This Class Is For Label2 """
    pass


class Normal3(Emphasis3):
    """ This Class Is For Region Object """


class Normal4(BaseOption):
    """ This Class Is For Label3 """

    def __init__(self):
        self.position = None
        self.show = None
        self.interval = None
        self.rotate = None
        self.formatter = None
        self.textStyle = TextStyle2()

    @check_args
    def set_keys(self, position=None, show: bool=None, interval=None, rotate=None, formatter=None):
        self.position = position
        self.show = show
        self.interval = interval
        self.rotate = rotate
        self.formatter = formatter


class Normal5(Emphasis5):
    """ This Class Is For ControlStyle """


class ScaleLimit(BaseOption):
    def __init__(self):
        self.min = None
        self.max = None

    @check_args
    def set_keys(self, _min: int=None, _max: int=None):
        self.min = _min
        self.max = _max


class Regions(BaseOption2):
    pass


class ParallelAxisDefault(BaseOption):
    """ This Class Is For Parallel """

    def __init__(self):
        self.type = None
        self.name = None
        self.nameLocation = None
        self.nameTextStyle = TextStyle()
        self.nameGap = None
        self.nameRotate = None
        self.inverse = None
        self.boundaryGap = None
        self.min = None
        self.max = None
        self.scale = None
        self.splitNumber = None
        self.minInterval = None
        self.interval = None
        self.logBase = None
        self.silent = None
        self.triggerEvent = None
        self.axisLine = AxisLine()
        self.axisTick = AxisTick2()
        self.axisLabel = AxisLabel2()
        self.data = Data()

    @check_args
    def set_keys(self, _type: str=None, name: str=None, name_location: str=None, name_gap: int=None,
                 name_rotate: int=None, inverse: bool=None, boundary_gap=None, _min=None, _max=None,
                 scale: bool=None, split_num: int=None, min_interval: int=None, interval: int=None,
                 log_base: int=None, silent: bool=None, trigger_event: bool=None):
        self.type = _type
        self.name = name
        self.nameLocation = name_location
        self.nameGap = name_gap
        self.nameRotate = name_rotate
        self.inverse = inverse
        self.boundaryGap = boundary_gap
        self.min = _min
        self.max = _max
        self.scale = scale
        self.splitNumber = split_num
        self.minInterval = min_interval
        self.interval = interval
        self.logBase = log_base
        self.silent = silent
        self.triggerEvent = trigger_event


class AreaSelectStyle(BaseOption):
    """ This Class Is For ParallelAxis """

    def __init__(self):
        self.width = None
        self.borderWidth = None
        self.borderColor = None
        self.color = None
        self.opacity = None

    @check_args
    def set_keys(self, width: int=None, border_width: int=None, border_color: str=None,
                 color: str=None, opacity: int=None):
        self.width = width
        self.borderWidth = border_width
        self.borderColor = border_color
        self.color = color
        self.opacity = opacity


class CheckPointStyle(BaseOption):
    """ This Class Is For Timeline """

    def __init__(self):
        self.symbol = None
        self.symbolSize = None
        self.symbolRotate = None
        self.symbolOffset = None
        self.color = None
        self.borderWidth = None
        self.borderColor = None
        self.animation = None
        self.animationDuration = None
        self.animationEasing = None

    @check_args
    def set_keys(self, symbol: str=None, symbol_size=None, symbol_rotate: int=None, symbol_offset: list=None,
                 color: str=None, border_width: int=None, border_color: str=None, animation: bool=None,
                 animation_duration: int=None, animation_easing: str=None):
        self.symbol = symbol
        self.symbolSize = symbol_size
        self.symbolRotate = symbol_rotate
        self.symbolOffset = symbol_offset
        self.color = color
        self.borderWidth = border_width
        self.borderColor = border_color
        self.animation = animation
        self.animationDuration = animation_duration
        self.animationEasing = animation_easing


class ControlStyle(BaseOption):
    """ This Class Is For Timeline """

    def __init__(self):
        self.show = None
        self.showPlayBtn = None
        self.showPrevBtn = None
        self.showNextBtn = None
        self.itemSize = None
        self.itemGap = None
        self.position = None
        self.playIcon = None
        self.stopIcon = None
        self.prevIcon = None
        self.nextIcon = None
        self.normal = Normal5()
        self.emphasis = Emphasis5()

    @check_args
    def set_keys(self, show: bool=None, show_play_btn: bool=None, show_prev_btn: bool=None,
                 show_next_btn: bool=None, item_size: int=None, item_gap: int=None, position: str=None,
                 play_icon: str=None, stop_icon: str=None, prev_icon: str=None, next_icon: str=None):
        self.show = show
        self.showPlayBtn = show_play_btn
        self.showPrevBtn = show_prev_btn
        self.showNextBtn = show_next_btn
        self.itemSize = item_size
        self.itemGap = item_gap
        self.position = position
        self.playIcon = play_icon
        self.stopIcon = stop_icon
        self.prevIcon = prev_icon
        self.nextIcon = next_icon


class GraphicStyle(BaseOption):
    def __init__(self):
        self.x = None
        self.y = None
        self.fill = None
        self.stroke = None
        self.lineWidth = None
        self.shadowBlur = None
        self.shadowOffsetX = None
        self.shadowOffsetY = None
        self.shadowColor = None

    @check_args
    def set_keys(self, x: int=None, y: int=None, fill: str=None, stroke: str=None, line_width: int=None,
                 shadow_blur: int=None, shadow_offset_x: int=None, shadow_offset_y: int=None, shadow_color: int=None):
        self.x = x
        self.y = y
        self.fill = fill
        self.stroke = stroke
        self.lineWidth = line_width
        self.shadowBlur = shadow_blur
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y
        self.shadowColor = shadow_color


class GraphicImageStyle(GraphicStyle):
    def __init__(self):
        super().__init__()
        self.image = None
        self.width = None
        self.height = None

    @check_args
    def set_keys(self, image: str=None, x: int=None, y: int=None, width: int=None, height: int=None,
                 fill: str=None, stroke: str=None, line_width: int=None, shadow_blur: int=None,
                 shadow_offset_x: int=None, shadow_offset_y: int=None, shadow_color: int=None):
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = fill
        self.stroke = stroke
        self.lineWidth = line_width
        self.shadowBlur = shadow_blur
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y
        self.shadowColor = shadow_color


class GraphicTextStyle(GraphicStyle):
    def __init__(self):
        super().__init__()
        self.text = None
        self.font = None
        self.textAlign = None
        self.textVerticalAlign = None

    @check_args
    def set_keys(self, x: int=None, y: int=None, fill: str=None, stroke: str=None, line_width: int=None,
                 shadow_blur: int=None, shadow_offset_x: int=None, shadow_offset_y: int=None, shadow_color: int=None,
                 text: str=None, font: str=None, text_align: str=None, text_vertical_align: str=None):
        self.x = x
        self.y = y
        self.fill = fill
        self.stroke = stroke
        self.lineWidth = line_width
        self.shadowBlur = shadow_blur
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y
        self.shadowColor = shadow_color
        self.text = text
        self.font = font
        self.textAlign = text_align
        self.textVerticalAlign = text_vertical_align


class GraphicRectStyle(BaseOption):
    def __init__(self):
        self.fill = None
        self.stroke = None
        self.lineWidth = None
        self.shadowBlur = None
        self.shadowOffsetX = None
        self.shadowOffsetY = None
        self.shadowColor = None

    @check_args
    def set_keys(self, fill: str=None, stroke: str=None, line_width: int=None,
                 shadow_blur: int=None, shadow_offset_x: int=None, shadow_offset_y: int=None, shadow_color: int=None):
        self.fill = fill
        self.stroke = stroke
        self.lineWidth = line_width
        self.shadowBlur = shadow_blur
        self.shadowOffsetX = shadow_offset_x
        self.shadowOffsetY = shadow_offset_y
        self.shadowColor = shadow_color


class GraphicCircleStyle(GraphicRectStyle):
    pass


class GraphicRingStyle(GraphicRectStyle):
    pass


class GraphicSectorStyle(GraphicRectStyle):
    pass


class GraphicArcStyle(GraphicRectStyle):
    pass


class GraphicPolygonStyle(GraphicRectStyle):
    pass


class GraphicPolyLineStyle(GraphicRectStyle):
    pass


class GraphicLineStyle(GraphicRectStyle):
    pass


class GraphicBezierCurveStyle(GraphicRectStyle):
    pass


class GraphicRectShape(BaseOption):
    def __init__(self):
        self.x = None
        self.y = None
        self.width = None
        self.height = None

    @check_args
    def set_keys(self, x: int=None, y: int=None, width: int=None, height: int=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class GraphicCircleShape(BaseOption):
    def __init__(self):
        self.cx = None
        self.cy = None
        self.r = None

    @check_args
    def set_keys(self, cx: int=None, cy: int=None, r: int=None):
        self.cx = cx
        self.cy = cy
        self.r = r


class GraphicRingShape(GraphicCircleShape):
    def __init__(self):
        super().__init__()
        self.r0 = None

    @check_args
    def set_keys(self, cx: int=None, cy: int=None, r: int=None, r0: int=None):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.r0 = r0


class GraphicSectorShape(GraphicRingShape):
    def __init__(self):
        super().__init__()
        self.startAngle = None
        self.endAngle = None
        self.clockwise = None

    @check_args
    def set_keys(self, cx: int=None, cy: int=None, r: int=None, r0: int=None, start_angle: int=None,
                 end_angle: int=None, clock_wise: bool=None):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.r0 = r0
        self.startAngle = start_angle
        self.endAngle = end_angle
        self.clockwise = clock_wise


class GraphicArcShape(GraphicSectorShape):
    pass


class GraphicPolygonShape(BaseOption):
    def __init__(self):
        self.points = None
        self.smooth = None
        self.smoothConstraint = None

    @check_args
    def set_keys(self, points: list=None, smooth=None, smooth_constraint: bool=None):
        self.points = points
        self.smooth = smooth
        self.smoothConstraint = smooth_constraint


class GraphicPolyLineShape(GraphicPolygonShape):
    pass


class GraphicLineShape(BaseOption):
    def __init__(self):
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.percent = None

    @check_args
    def set_keys(self, x1: int=None, y1: int=None, x2: int=None, y2: int=None, percent: int=None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.percent = percent


class GraphicBezierCurveShape(GraphicLineShape):
    def __init__(self):
        super().__init__()
        self.cpx1 = None
        self.cpy1 = None
        self.cpx2 = None
        self.cpy2 = None

    @check_args
    def set_keys(self, x1: int=None, y1: int=None, x2: int=None, y2: int=None, percent: int=None, cpx1: int=None,
                 cpy1: int=None, cpx2: int=None, cpy2: int=None, ):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.percent = percent
        self.cpx1 = cpx1
        self.cpy1 = cpy1
        self.cpx2 = cpx2
        self.cpy2 = cpy2
