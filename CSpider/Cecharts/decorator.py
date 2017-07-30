# -*- utf-8 -*-

import inspect

from functools import wraps


def check_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        _list = inspect.getfullargspec(func)[0][1:]
        if args[1:]:
            for i, v in enumerate(_list[:len(args[1:])]):
                if func.__annotations__.get(v, None):
                    if not isinstance(args[1:][i], func.__annotations__[v]):
                        raise TypeError("{0} = {3} is must be {1}, get {2} type. ".format(
                            v, func.__annotations__[v].__name__, type(args[1:][i]).__name__, args[1:][i]))
        if kwargs:
            for index, arg in enumerate(_list):
                if func.__annotations__.get(arg, None) and kwargs.get(arg, None):
                    if not isinstance(kwargs[arg], func.__annotations__[arg]):
                        raise TypeError("{0} = {3} is must be {1}, get {2} type. ".format(
                            arg, func.__annotations__[arg].__name__, type(kwargs[arg]).__name__, kwargs[arg]))
        return func(*args, **kwargs)
    return wrapper
