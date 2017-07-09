# -*- coding:utf-8 -*-

import os
import glob

wrong_file = ['SpiderWorkers', '__init__']

try:
    # glob.glob得到当前目录下匹配字符串的文件名
    for module_file in glob.glob(os.path.join(os.path.dirname(__file__), '*.py')):
        module_name, _ = os.path.splitext(os.path.basename(module_file))
        if module_name not in wrong_file:
            # print(os.path.basename(module_name))
            __import__('Spider.' + module_name)
except Exception as err:
    print(err)
