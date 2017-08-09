# -*- utf-8 -*-

from .base_option import BaseOption
from Htmlrender.Cecharts.options.base_option import ParallelAxisDefault
from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/7'
__Version__ = '0.1'


class Parallel(BaseOption):
    def __init__(self):
        self.zlevel = None
        self.z = None
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None
        self.width = None
        self.height = None
        self.layout = None
        self.axisExpandable = None
        self.axisExpandCenter = None
        self.axisExpandCount = None
        self.axisExpandWidth = None
        self.axisExpandTriggerOn = None
        self.parallelAxisDefault = ParallelAxisDefault()

    @check_args
    def set_keys(self, z_level: int=None, z: int=None, left=None, top=None, right=None, bottom=None,
                 width=None, height=None, layout: str=None, axis_expandable: bool=None, axis_expand_center: int=None,
                 axis_expand_count: int=None, axis_expand_width: int=None, axis_expand_trigger_on: str=None):
        self.zlevel = z_level
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.width = width
        self.height = height
        self.layout = layout
        self.axisExpandable = axis_expandable
        self.axisExpandCenter = axis_expand_center
        self.axisExpandCount = axis_expand_count
        self.axisExpandWidth = axis_expand_width
        self.axisExpandTriggerOn = axis_expand_trigger_on
