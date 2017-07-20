# -*- coding:utf-8 -*-

from collections import defaultdict

from Utils.BaseService import BaseService
from Utils.BaseManager import BaseManager

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/19'
__Version__ = '0.1'


class ServiceManager(BaseManager):
    """ Service Manager """

    def __init__(self):
        super().__init__()
        self._module_import(module_dir=['Service'],
                            wrong_file=['__init__', '__pycache__'],
                            packages=True)
        self.services = self._create_dict()

    def _create_dict(self):
        """ Initial Application Service Dict 
            
            Example:
                {'Monitor': ''}
        """

        _dict = defaultdict(dict)
        _dict.update({_.__name__: '' for _ in BaseService.__subclasses__()})
        return _dict

    def register_service(self, obj):
        """ Register Service 
            
            Example:
                {'Monitor': <class 'Service.Monitor.monitor.Monitor'>}
        """

        self.services[obj.__class__.__name__] = obj
