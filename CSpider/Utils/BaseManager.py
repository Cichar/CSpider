# -*- utf-8 -*-

import os
import abc
import glob

from Utils.Singleton import ABC

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/20'
__version__ = '0.1'


class BaseManager(object, metaclass=ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def _create_dict(self):
        pass

    @staticmethod
    def _module_import(module_dir=None, wrong_file=None, packages=False):
        """ Import Modules For Manager Dict """

        for _dir in module_dir:
            if packages:
                _path = r'{0}\*'
            else:
                _path = r'{0}\*.py'
            for module_file in glob.glob(_path.format(_dir)):
                module_name, _ = os.path.splitext(os.path.basename(module_file))
                if wrong_file:
                    if module_name not in wrong_file:
                        __import__('{0}.'.format(_dir) + module_name)
                else:
                    __import__('{0}.'.format(_dir) + module_name)
