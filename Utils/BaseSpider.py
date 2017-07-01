# -*- coding:utf-8 -*-

import abc
import json
from random import choice
from urllib.request import urlopen, Request

from Database import DataBase
from Conf.headers.headers import headers
from Conf.headers.user_agent import user_agent

""" 
   **  爬虫基类  **

    初始化BaseSpider，会提供数据库连接实例

    基类中提供：
                构造随机头的函数    create_header()
                解析URL的函数       parse_url()

"""

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/6/27'
__version__ = '0.1'


class BaseSpider(object, metaclass=abc.ABCMeta):

    @property
    def db(self):
        return DataBase()

    @property
    @abc.abstractmethod
    def name(self):
        """ 子类需设置爬虫名称 """
        return 'BaseSpider'

    @staticmethod
    def create_header(flag='default'):
        """ 

        构建随机头，根据flag的不同，提供不同网站的随机header

        """

        header = headers[flag]
        header['User-Agent'] = choice(user_agent)
        return header

    def parse_url(self, url=None, timeout=2, charset='utf-8', header=None, parse_json=False):
        """ 

        解析URL，默认超时2秒，默认解析编码UTF-8
        如提供头部参数，则构建包含自定义的头部请求，否则默认不包含自定义头部
        默认模式不解析json数据

        """

        try:
            if header:
                url = Request(url=url, headers=self.create_header(flag=header))
            response = urlopen(url, timeout=timeout)
            data = response.read().decode(charset, 'ignore')
            # 如果需要用json解析
            if parse_json:
                json_data = json.loads(data)
                return json_data
            else:
                return data
        except Exception as err:
            print('** parse_url : %s **' % str(err))
            raise Exception(err)
