# -*- utf-8 -*-

import abc

from Utils.Singleton import ABC

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/20'
__version__ = '0.1'


class BaseManager(object, metaclass=ABC):
    def __init__(self):
        self._module_import()

    @abc.abstractmethod
    def _create_dict(self):
        pass

    @abc.abstractmethod
    def _module_import(self):
        pass
