# -*- coding:utf-8 -*-

try:
    import Form
    import Spider
except Exception as err:
    print(err)

from Utils.BaseForm import BaseForm
from Utils.Singleton import Singleton
from Utils.BaseSpider import BaseSpider

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/1'
__Version__ = '0.1'


class SpiderManager(object, metaclass=Singleton):
    """ Spider Manager """

    def __init__(self):
        self.spiders = self.__create_spider_dict()

    @staticmethod
    def __create_spider_dict():
        """ Create Spider Dict 
            
            Example:
              {'NetEaseMusicCloud': {'spider': <class 'Spider.NetEaseMusicCloud.NetEaseMusicCloudSpider'>, 
                                     'form': <class 'Form.TaskForm.NetEaseMusicCloudForm'>}, 
               'ZhiHuUser': {'spider': <class 'Spider.Zhihu.ZhiHuSpider'>, 
                             'form': <class 'Form.TaskForm.ZhiHuForm'>}
              }
        """

        spiders = {spider.name: spider for spider in BaseSpider.__subclasses__()}
        forms = {form.name: form for form in BaseForm.__subclasses__()}

        for spider in spiders:
            spiders[spider] = {'spider': spiders[spider](), 'form': forms[spider]}
        return spiders
