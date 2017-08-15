# -*- utf-8 -*-

from .base_object import BaseObject
from Htmlrender.decorator import check_args
from Htmlrender.Cecharts.options.base_option import Data
from Htmlrender.Cecharts.options.base_option import GraphicRectShape
from Htmlrender.Cecharts.options.base_option import GraphicCircleShape
from Htmlrender.Cecharts.options.base_option import GraphicRingShape
from Htmlrender.Cecharts.options.base_option import GraphicSectorShape
from Htmlrender.Cecharts.options.base_option import GraphicArcShape
from Htmlrender.Cecharts.options.base_option import GraphicPolygonShape
from Htmlrender.Cecharts.options.base_option import GraphicPolyLineShape
from Htmlrender.Cecharts.options.base_option import GraphicLineShape
from Htmlrender.Cecharts.options.base_option import GraphicBezierCurveShape
from Htmlrender.Cecharts.options.base_option import GraphicImageStyle
from Htmlrender.Cecharts.options.base_option import GraphicTextStyle
from Htmlrender.Cecharts.options.base_option import GraphicRectStyle
from Htmlrender.Cecharts.options.base_option import GraphicCircleStyle
from Htmlrender.Cecharts.options.base_option import GraphicRingStyle
from Htmlrender.Cecharts.options.base_option import GraphicSectorStyle
from Htmlrender.Cecharts.options.base_option import GraphicArcStyle
from Htmlrender.Cecharts.options.base_option import GraphicPolygonStyle
from Htmlrender.Cecharts.options.base_option import GraphicPolyLineStyle
from Htmlrender.Cecharts.options.base_option import GraphicLineStyle
from Htmlrender.Cecharts.options.base_option import GraphicBezierCurveStyle


__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/9'
__Version__ = '0.1'


class BaseGraphic(BaseObject):
    """ This Class Is The BaseGraphic Object Class For Graphic Option 
        The Child Class Need To Provide ''type'' Arg.
    """

    def __init__(self):
        self.id = None
        self.action = None
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None
        self.bounding = None
        self.z = None
        self.zlevel = None
        self.silent = None
        self.invisible = None
        self.cursor = None
        self.draggable = None
        self.progressive = None
        self.onclick = None
        self.onmouseover = None
        self.onmouseout = None
        self.onmousemove = None
        self.onmousewheel = None
        self.onmousedown = None
        self.onmouseup = None
        self.ondrag = None
        self.ondragstart = None
        self.ondragend = None
        self.ondragenter = None
        self.ondragleave = None
        self.ondragover = None
        self.ondrop = None

    @check_args
    def set_keys(self, _id: str=None, action: str=None, left=None, right=None, top=None, bottom=None,
                 bounding: str=None, z: int=None, z_level: int=None, silent: bool=None, invisible: bool=None,
                 cursor: str=None, draggable: bool=None, progressive: bool=None, onclick=None, on_mouse_over=None,
                 on_mouse_out=None, on_mouse_move=None, on_mouse_wheel=None, on_mouse_down=None, on_mouse_up=None,
                 ondrag=None, ondrag_start=None, ondrag_end=None, ondrag_enter=None, ondrag_leave=None,
                 ondrag_over=None, on_drop=None):
        self.id = _id
        self.action = action
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.bounding = bounding
        self.z = z
        self.zlevel = z_level
        self.silent = silent
        self.invisible = invisible
        self.cursor = cursor
        self.draggable = draggable
        self.progressive = progressive
        self.onclick = onclick
        self.onmouseover = on_mouse_over
        self.onmouseout = on_mouse_out
        self.onmousemove = on_mouse_move
        self.onmousewheel = on_mouse_wheel
        self.onmousedown = on_mouse_down
        self.onmouseup = on_mouse_up
        self.ondrag = ondrag
        self.ondragstart = ondrag_start
        self.ondragend = ondrag_end
        self.ondragenter = ondrag_enter
        self.ondragleave = ondrag_leave
        self.ondragover = ondrag_over
        self.ondrop = on_drop

    @property
    def json(self):
        _json = {}
        for k, v in self.__dict__.items():
            if v:
                if hasattr(v, 'json'):
                    if v.json:
                        if k == 'action':
                            _json['$action'] = v.json
                        else:
                            _json[k] = v.json
                else:
                    if k == 'action':
                        _json['$action'] = v
                    else:
                        _json[k] = v
        return _json


class GroupGraphic(BaseGraphic):
    def __init__(self):
        super().__init__()
        self.type = 'group'
        self.width = None
        self.height = None
        self.children = Data()

    @check_args
    def set_keys(self, _id: str=None, action: str=None, left=None, right=None, top=None, bottom=None,
                 bounding: str=None, z: int=None, z_level: int=None, silent: bool=None, invisible: bool=None,
                 cursor: str=None, draggable: bool=None, progressive: bool=None, onclick=None, on_mouse_over=None,
                 on_mouse_out=None, on_mouse_move=None, on_mouse_wheel=None, on_mouse_down=None, on_mouse_up=None,
                 ondrag=None, ondrag_start=None, ondrag_end=None, ondrag_enter=None, ondrag_leave=None,
                 ondrag_over=None, on_drop=None, width: int=None, height: int=None):
        self.id = _id
        self.action = action
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.bounding = bounding
        self.z = z
        self.zlevel = z_level
        self.silent = silent
        self.invisible = invisible
        self.cursor = cursor
        self.draggable = draggable
        self.progressive = progressive
        self.width = width
        self.height = height
        self.onclick = onclick
        self.onmouseover = on_mouse_over
        self.onmouseout = on_mouse_out
        self.onmousemove = on_mouse_move
        self.onmousewheel = on_mouse_wheel
        self.onmousedown = on_mouse_down
        self.onmouseup = on_mouse_up
        self.ondrag = ondrag
        self.ondragstart = ondrag_start
        self.ondragend = ondrag_end
        self.ondragenter = ondrag_enter
        self.ondragleave = ondrag_leave
        self.ondragover = ondrag_over
        self.ondrop = on_drop


class ImageGraphic(BaseGraphic):
    def __init__(self):
        super().__init__()
        self.type = 'image'
        self.style = GraphicImageStyle()


class TextGraphic(BaseGraphic):
    def __init__(self):
        super().__init__()
        self.type = 'text'
        self.style = GraphicTextStyle()


class RectGraphic(BaseGraphic):
    def __init__(self):
        super().__init__()
        self.type = 'rect'
        self.shape = GraphicRectShape()
        self.style = GraphicRectStyle()


class CircleGraphic(BaseGraphic):
    def __init__(self):
        super().__init__()
        self.type = 'circle'
        self.shape = GraphicCircleShape()
        self.style = GraphicCircleStyle()


class RingGraphic(BaseGraphic):
    def __init__(self):
        super().__init__()
        self.type = 'ring'
        self.shape = GraphicRingShape()
        self.style = GraphicRingStyle()


class SectorGraphic(BaseGraphic):
    def __init__(self):
        super().__init__()
        self.type = 'sector'
        self.shape = GraphicSectorShape()
        self.style = GraphicSectorStyle()


class ArcGraphic(BaseGraphic):
    def __init__(self):
        super().__init__()
        self.type = 'arc'
        self.shape = GraphicArcShape()
        self.style = GraphicArcStyle()


class PolygonGraphic(BaseGraphic):
    def __init__(self):
        super().__init__()
        self.type = 'polygon'
        self.shape = GraphicPolygonShape()
        self.style = GraphicPolygonStyle()


class PolylineGraphic(BaseGraphic):
    def __init__(self):
        super().__init__()
        self.type = 'polyline'
        self.shape = GraphicPolyLineShape()
        self.style = GraphicPolyLineStyle()


class LineGraphic(BaseGraphic):
    def __init__(self):
        super().__init__()
        self.type = 'line'
        self.shape = GraphicLineShape()
        self.style = GraphicLineStyle()


class BezierCurveGraphic(BaseGraphic):
    def __init__(self):
        super().__init__()
        self.type = 'beziercurve'
        self.shape = GraphicBezierCurveShape()
        self.style = GraphicBezierCurveStyle()
