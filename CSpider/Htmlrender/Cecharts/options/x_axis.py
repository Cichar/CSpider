# -*- utf-8 -*-

from .base_option import BaseOption
from .base_option import TextStyle
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class XAxis(BaseOption):
    def __init__(self):
        self.show = None
        self.gridIndex = None
        self.position = None
        self.offset = None
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
        self.axisLine = None
        self.axisTick = None
        self.axisLabel = None
        self.splitLine = None
        self.splitArea = None
        self.data = None
        self.axisPointer = None
        self.zlevel = None
        self.z = None

    @check_args
    def set_keys(self, *args, **kwargs):
        pass
