# -*- utf-8 -*-

from .base_option import BaseOption
from .base_option import Label
from .base_option import LineStyle
from .base_option import ShadowStyle
from .base_option import CrossStyle
from .base_option import Handle
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class AxisPointer(BaseOption):
    """ This Class Is For Grid, ToolTip """

    def __init__(self):
        self.type = None
        self.axis = None
        self.snap = None
        self.z = None
        self.label = Label()
        self.lineStyle = LineStyle()
        self.shadowStyle = ShadowStyle()
        self.crossStyle = CrossStyle()

    @check_args
    def set_keys(self, _type: str=None, axis: str=None, snap: bool=None, z: int=None):
        self.type = _type
        self.axis = axis
        self.snap = snap
        self.z = z


class AxisPointer2(BaseOption):
    """ This Class Is For xAxis, yAxis, RadiusAxis, AngleAxis """

    def __init__(self):
        self.show = None
        self.type = None
        self.snap = None
        self.z = None
        self.label = Label()
        self.lineStyle = LineStyle()
        self.shadowStyle = ShadowStyle()
        self.triggerTooltip = None
        self.value = None
        self.status = None
        self.handle = Handle()

    def set_keys(self, show: bool=None, _type: str=None, snap: bool=None, z: int=None,
                 trigger_tooltip: bool=None, value: int=None, status: bool=None):
        self.show = show
        self.type = _type
        self.snap = snap
        self.z = z
        self.triggerTooltip = trigger_tooltip
        self.value = value
        self.status = status


class AxisPointer3(AxisPointer2):
    """ This Class Is For Main AxisPinter """

    def __init__(self):
        super().__init__()
        self.link = None
        self.triggerOn = None

    def set_keys(self, show: bool=None, _type: str=None, snap: bool=None, z: int=None,
                 trigger_tooltip: bool=None, value: int=None, status: bool=None, link: list=None,
                 trigger_on: str=None):
        self.show = show
        self.type = _type
        self.snap = snap
        self.z = z
        self.triggerTooltip = trigger_tooltip
        self.value = value
        self.status = status
        self.link = link
        self.triggerOn = trigger_on
