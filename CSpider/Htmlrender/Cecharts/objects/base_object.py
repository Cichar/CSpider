# -*- utf-8 -*-

import abc
import json

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/8'
__Version__ = '0.1'


class BaseObject(object):
    """ For Dict Object """

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

