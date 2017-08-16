# -*- utf-8 -*-

from Htmlrender.decorator import check_args

from Htmlrender.Cecharts.options.geo import Geo
from Htmlrender.Cecharts.options.grid import Grid
from Htmlrender.Cecharts.options.title import Title
from Htmlrender.Cecharts.options.polar import Polar
from Htmlrender.Cecharts.options.radar import Radar
from Htmlrender.Cecharts.options.brush import Brush
from Htmlrender.Cecharts.options.x_axis import XAxis
from Htmlrender.Cecharts.options.y_axis import YAxis
from Htmlrender.Cecharts.options.series import Series
from Htmlrender.Cecharts.options.legend import Legend
from Htmlrender.Cecharts.options.graphic import Graphic
from Htmlrender.Cecharts.options.toolbox import ToolBox
from Htmlrender.Cecharts.options.tooltip import ToolTip2
from Htmlrender.Cecharts.options.calendar import Calendar
from Htmlrender.Cecharts.options.parallel import Parallel
from Htmlrender.Cecharts.options.timeline import TimeLine
from Htmlrender.Cecharts.options.data_zoom import DataZoom
from Htmlrender.Cecharts.options.angle_axis import AngleAxis
from Htmlrender.Cecharts.options.visual_map import VisualMap
from Htmlrender.Cecharts.options.base_option import TextStyle
from Htmlrender.Cecharts.options.radius_axis import RadiusAxis
from Htmlrender.Cecharts.options.single_axis import SingleAxis
from Htmlrender.Cecharts.options.axis_pointer import AxisPointer3
from Htmlrender.Cecharts.options.parallel_axis import ParallelAxis

from Htmlrender.Cecharts.BaseRender import RENDER_TO_WEB

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class BaseChart(object):
    """ This Base Charts Class For Automatic Render EChart Lib. """

    _fields = ['title', 'legend', 'grid', 'xAxis', 'yAxis', 'polar', 'radiusAxis', 'angleAxis',
               'radar', 'dataZoom', 'visualMap', 'tooltip', 'axisPointer', 'toolbox', 'brush',
               'geo', 'parallel', 'parallelAxis', 'singleAxis', 'timeline', 'graphic', 'calendar',
               'series', 'color', 'backgroundColor', 'textStyle', 'animation', 'animationThreshold',
               'animationDuration', 'animationEasing', 'animationDelay', 'animationDurationUpdate',
               'animationEasingUpdate', 'animationDelayUpdate', 'progressive', 'progressiveThreshold',
               'blendMode', 'hoverLayerThreshold', 'useUTC']

    @check_args
    def __init__(self, title: str, subtitle: str = None, toolbox: bool = True, name: str = 'myChart',
                 width: str = '100%', height: str = '400px', render_id: str = None, color: list=None,
                 background_color=None, animation: bool = False, animation_threshold: int = None,
                 animation_duration: int = None, animation_easing: str = None, animation_delay: int = None,
                 animation_duration_update: int = None, animation_easing_update: str = None,
                 animation_delay_update: int = None, progressive: int = None,  progressive_threshold: int = None,
                 blend_mode: str = None, hover_layer_threshold: int = None, use_utc: bool = None):
        """
        :param title: 
                    Chart's Title.
        :param subtitle: 
                    Charts's subtitle.
        :param toolbox: 
                    Show Or Not Show Chart's Toolbox. Default Is ''True''.
        :param name: 
                    The Name For Render In Web Page. Default Is ''myChart''.
                    User Need To Provide Another Name To Support When The 
                    Web Page Has More Than One Chart.
        :param width: 
                    The Width For Render In Web Page. Default Is ''100%''.
        :param height: 
                    The Height For Render In Web Page. Default Is ''400px''.
        :param render_id: 
                    The Id For JS To Select, Then ECharts Initial The Object.
        :param animation: 
                    Whether to enable animation.
        :param animation_threshold: 
                    Whether to set graphic number threshold to animation. 
                    Animation will be disabled when graphic number is larger than threshold.
        :param animation_duration: 
                    Duration of the first animation, which supports callback function for 
                    different data to have different animation effect:
                        animationDuration: function (idx) {
                            // delay for later data is larger
                            return idx * 100;
                        }
        :param animation_easing: 
                    Easing method used for the first animation. 
                    Varied easing effects can be found at easing effect example.
        :param animation_delay: 
                    Delay before updating the first animation,  which supports callback 
                    function for different data to have different animation effect.
                    For example:
                        animationDelay: function (idx) {
                            // delay for later data is larger
                            return idx * 100;
                        }
        :param animation_duration_update: 
                    Time for animation to complete, which supports callback function 
                    for different data to have different animation effect:
                        animationDurationUpdate: function (idx) {
                            // delay for later data is larger
                            return idx * 100;
                        }
        :param animation_easing_update: 
                    Easing method used for animation.
        :param animation_delay_update: 
                    Delay before updating animation, which supports callback function for 
                    different data to have different animation effect.
                    For example:
                        animationDelayUpdate: function (idx) {
                            // delay for later data is larger
                            return idx * 100;
                        }
        :param progressive: 
                    pass
        :param progressive_threshold: 
                    pass
        :param blend_mode:
                    pass
        :param hover_layer_threshold:
                    pass
        :param use_utc: 
                    Whether to use UTC in display.The default value of useUTC is false.
                    true: When axis.type is 'time', ticks is determined according to UTC, 
                          and axisLabel and tooltip use UTC by default.
                    false: When axis.type is 'time', ticks is determined according to local time, 
                           and axisLabel and tooltip use local time by default.
        """

        if not name:
            raise ValueError('name is required and must be string type.')
        if not render_id:
            raise ValueError('render_id is required and must be string type.')
        if not width:
            raise ValueError('width is required and must be string type, such as "100%" or "400px"')
        if not height:
            raise ValueError('height is required and must be string type, such as "20%" or "400px"')
        self._name = name
        self._width = width
        self._height = height
        self._render_id = render_id

        self.title = Title(title=title, subtitle=subtitle)
        self.legend = Legend()
        self.grid = Grid()
        self.xAxis = XAxis()
        self.yAxis = YAxis()
        self.polar = Polar()
        self.radiusAxis = RadiusAxis()
        self.angleAxis = AngleAxis()
        self.radar = Radar()
        self.dataZoom = DataZoom()
        self.visualMap = VisualMap()
        self.tooltip = ToolTip2()
        self.axisPointer = AxisPointer3()
        self.toolbox = ToolBox()
        if toolbox:
            self.toolbox.show = True
        else:
            self.toolbox.show = False
        self.brush = Brush()
        self.geo = Geo()
        self.parallel = Parallel()
        self.parallelAxis = ParallelAxis()
        self.singleAxis = SingleAxis()
        self.timeline = TimeLine()
        self.graphic = Graphic()
        self.calendar = Calendar()
        self.series = Series()
        self.color = color
        self.backgroundColor = background_color
        self.textStyle = TextStyle()

        self.animation = animation
        self.animationThreshold = animation_threshold
        self.animationDuration = animation_duration
        self.animationEasing = animation_easing
        self.animationDelay = animation_delay
        self.animationDurationUpdate = animation_duration_update
        self.animationEasingUpdate = animation_easing_update
        self.animationDelayUpdate = animation_delay_update

        self.progressive = progressive
        self.progressiveThreshold = progressive_threshold
        self.blendMode = blend_mode
        self.hoverLayerThreshold = hover_layer_threshold
        self.useUTC = use_utc

    @property
    def option(self):
        _option = {}
        for field in self._fields:
            obj = getattr(self, field)
            if hasattr(obj, 'json'):
                if obj.json:
                    if callable(obj.json):
                        _option[field] = obj.json()
                    else:
                        _option[field] = obj.json
            elif hasattr(obj, 'array'):
                if obj.array:
                    _option[field] = obj.array
            else:
                if obj:
                    _option[field] = obj
        return _option

    def render_to_web(self):
        """ Render Chart To Web """

        return RENDER_TO_WEB.format(render_id=self._render_id, width=self._width,
                                    height=self._height, name=self._name, option=self.option)

    def __str__(self):
        return '%s' % self.option


if __name__ == '__main__':
    a = BaseChart('Test', subtitle='1234', render_id='test1')
    print(a)
