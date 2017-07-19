# -*- utf-8 -*-

import os

try:
    dir_list = [_ for _ in os.listdir(os.path.dirname(__file__)) if not _.startswith('__')]
    for _ in dir_list:
        __import__('Service.' + _)
except Exception as err:
    print(err)
