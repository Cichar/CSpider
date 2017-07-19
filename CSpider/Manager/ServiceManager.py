# -*- coding:utf-8 -*-

try:
    import Service
except Exception as err:
    print(err)

from collections import defaultdict

from Utils.Singleton import Singleton
from Utils.BaseService import BaseService

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/19'
__Version__ = '0.1'


class ServiceManager(object, metaclass=Singleton):
    """ Service Manager """

    def __init__(self):
        self.services = self.__create_service_dict()

    @staticmethod
    def __create_service_dict():
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
