# -*- utf-8 -*-

from .base_option import BaseOption
from .base_option import TextStyle
from .axis_pointer import AxisPointer
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class ToolTip(BaseOption):
    """ This Class Is For Polar """

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
                 background_color: str=None, border_color: str=None, border_width: int=None,
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


class ToolTip2(ToolTip):
    """ This Is The Main Tooltip Option """

    def __init__(self):
        super().__init__()
        self.showContent = None
        self.alwaysShowContent = None
        self.triggerOn = None
        self.showDelay = None
        self.hideDelay = None
        self.enterable = None
        self.confine = None
        self.transitionDuration = None

    @check_args
    def set_keys(self, show: bool=None, trigger: str=None, position=None, formatter=None,
                 background_color: str=None, border_color: str=None, border_width: int=None,
                 padding: int=None, extra_css_text: str=None, show_content: bool=None,
                 always_show_content: bool=None, trigger_on: str=None, show_delay: int=None,
                 hide_delay: int=None, enterable: bool=None, confine: bool=None, transition_duration: int=None):
        self.show = show
        self.trigger = trigger
        self.position = position
        self.formatter = formatter
        self.backgroundColor = background_color
        self.borderColor = border_color
        self.borderWidth = border_width
        self.padding = padding
        self.extraCssText = extra_css_text
        self.showContent = show_content
        self.alwaysShowContent = always_show_content
        self.triggerOn = trigger_on
        self.showDelay = show_delay
        self.hideDelay = hide_delay
        self.enterable = enterable
        self.confine = confine
        self.transitionDuration = transition_duration
