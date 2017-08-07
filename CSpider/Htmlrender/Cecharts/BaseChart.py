# -*- utf-8 -*-

from Htmlrender.decorator import check_args
from options.title import Title
from options.legend import Legend
from options.grid import Grid
from options.x_axis import XAxis
from options.y_axis import YAxis
from options.text_style import TextStyle

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

    RENDER_HTML = """
                     <div id="{render_id}" style="width:{width};height:{height};"></div> 
                     <script type="text/javascript"> 
                        var {name} = echarts.init(document.getElementById('{render_id}'));
                        var option = {option}; 
                        {name}.setOption(option); 
                     </script>
                  """

    @check_args
    def __init__(self, title: str, subtitle: str = None, toolbox: bool = False, name: str = 'myChart',
                 width: str = '100%', height: str = '400px', render_id: str = None, animation: bool = False,
                 animation_threshold: int = None, animation_duration: int = None, animation_easing: str = None,
                 animation_delay: int = None, animation_duration_update: int = None,
                 animation_easing_update: str = None, animation_delay_update: int = None, progressive: int = None,
                 progressive_threshold: int = None, blend_mode: str = None, hover_layer_threshold: int = None,
                 use_utc: bool = None):
        """
        :param title: 
                    Chart's Title.
        :param subtitle: 
                    Charts's subtitle.
        :param toolbox: 
                    Show Or Not Show Chart's Toolbox. Default Is ''False''.
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
        :param animation_threshold: 
        :param animation_duration: 
        :param animation_easing: 
        :param animation_delay: 
        :param animation_duration_update: 
        :param animation_easing_update: 
        :param animation_delay_update: 
        :param progressive: 
        :param progressive_threshold: 
        :param blend_mode: 
        :param hover_layer_threshold: 
        :param use_utc: 
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
        self.polar = ''
        self.radiusAxis = ''
        self.angleAxis = ''
        self.radar = ''
        self.dataZoom = ''
        self.visualMap = ''
        self.tooltip = ''
        self.axisPointer = ''
        self.toolbox = ''
        self.brush = ''
        self.geo = ''
        self.parallel = ''
        self.parallelAxis = ''
        self.singleAxis = ''
        self.timeline = ''
        self.graphic = ''
        self.calendar = ''
        self.series = ''
        self.color = ''
        self.backgroundColor = ''
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
                    _option[field] = obj.json
            else:
                if obj:
                    _option[field] = obj
        return _option

    def render(self):
        """ Render Chart """

        return self.RENDER_HTML.format(render_id=self._render_id, width=self._width,
                                       height=self._height, name=self._name, option=self.option)

    def __str__(self):
        return '%s' % self.option


if __name__ == '__main__':
    a = BaseChart('Test', subtitle='1234', render_id='test1', toolbox=True)
    a.title.show = False
    a.title.textStyle.color = 'test'
    a.grid.tooltip.textStyle.fontSize = 12
    a.textStyle.set_keys(color='2131243')
    print(a)
