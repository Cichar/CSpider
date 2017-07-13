# -*- coding:utf-8 -*-

import abc

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/1'
__Version__ = '0.1'


class Singleton(type):
    """ Singleton metaclass """

    def __init__(cls, *args, **kwargs):
        super(Singleton, cls).__init__(*args, **kwargs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance


class ABC(abc.ABCMeta):
    """ Singleton metaclass base on abc.ABCMeta """

    def __init__(cls, name, bases, class_dict):
        super(ABC, cls).__init__(name, bases, class_dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ABC, cls).__call__(*args, **kwargs)
        return cls._instance
