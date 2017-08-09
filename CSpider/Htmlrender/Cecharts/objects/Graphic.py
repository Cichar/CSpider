# -*- utf-8 -*-

from .base_object import BaseObject
from Htmlrender.decorator import check_args

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
    def set_keys(self, *args, **kwargs):
        pass

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
