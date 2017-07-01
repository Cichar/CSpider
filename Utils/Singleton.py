# -*- coding:utf-8 -*-

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/1'
__Version__ = '0.1'


class Singleton(type):
    """ 单例设计模式所用元类 """

    def __init__(cls, *args, **kwargs):
        super(Singleton, cls).__init__(*args, **kwargs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance


class Test(object, metaclass=Singleton):
    pass


if __name__ == '__main__':
    a = Test()
    b = Test()
    print(id(a))
    print(id(b))
