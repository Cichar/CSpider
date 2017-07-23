# -*- coding:utf-8 -*-

import os
import glob

wrong_file = ['__init__']

try:
    for module_file in glob.glob(os.path.join(os.path.dirname(__file__), '*.py')):
        module_name, _ = os.path.splitext(os.path.basename(module_file))
        if module_name not in wrong_file:
            # print(module_name)
            __import__('CommonTask.' + module_name)
except Exception as err:
    print(err)
