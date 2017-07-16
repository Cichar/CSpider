# -*- coding:utf-8 -*-

import abc
import json
from random import choice
from urllib.request import urlopen, Request

from Utils.Singleton import ABC
from Utils.Exception import ParseUrlError
from Conf.headers.headers import headers
from Conf.headers.user_agent import user_agent

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/6/27'
__version__ = '0.1'


class BaseSpider(object, metaclass=ABC):

    @property
    @abc.abstractmethod
    def name(self):
        """ Subclass Need To Provide Name For The Spider """
        return 'BaseSpider'

    @abc.abstractmethod
    def task_distribute(self, data):
        """ Subclass Need To Implement This Function To Distribute Tasks. """
        pass

    @staticmethod
    def create_header(flag='default'):
        """ 
        
        Create Random Headers With Different User-Agent Depend On Flag Arg.

        """

        header = headers[flag]
        header['User-Agent'] = choice(user_agent)
        return header

    @classmethod
    def parse_url(cls, url=None, timeout=2, charset='utf-8', header=None, parse_json=False):
        """ 
        
        Parse URL Function
        Default : Timeout 2 Seconds
                  Parse Charset UTF-8
                  Not Parse Json-Object
        If Provide Header Args, Create Request With Headers Else Not.

        """

        try:
            if header:
                url = Request(url=url, headers=cls.create_header(flag=header))
            response = urlopen(url, timeout=timeout)
            data = response.read().decode(charset, 'ignore')
            # if need parse json-object
            if parse_json:
                json_data = json.loads(data)
                return json_data
            else:
                return data
        except Exception as err:
            raise ParseUrlError(err)


