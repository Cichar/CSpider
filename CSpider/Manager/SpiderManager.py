# -*- coding:utf-8 -*-

from Utils.BaseForm import BaseForm
from Utils.BaseSpider import BaseSpider
from Utils.BaseManager import BaseManager

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/1'
__Version__ = '0.1'


class SpiderManager(BaseManager):
    """ Spider Manager """

    _dir_list = ['Spider', 'Form']

    def __init__(self):
        super().__init__()
        self.spiders = self._create_dict()

    def _create_dict(self):
        """ Create Spider Dict 
            
            Example:
              {'NetEaseMusicCloud': {'spider': <class 'Spider.NetEaseMusicCloud.NetEaseMusicCloudSpider'>, 
                                     'form': <class 'Form.TaskForm.NetEaseMusicCloudForm'>}, 
               'ZhiHuUser': {'spider': <class 'Spider.Zhihu.ZhiHuSpider'>, 
                             'form': <class 'Form.TaskForm.ZhiHuForm'>}
              }
        """

        try:
            import os
            import glob

            for _dir in self._dir_list:
                for module_file in glob.glob(r'{0}\*.py'.format(_dir)):
                    module_name, _ = os.path.splitext(os.path.basename(module_file))
                    if module_name != '__init__':
                        __import__('{0}.'.format(_dir) + module_name)
        except Exception as err:
            print(err)
        else:
            spiders = {spider.name: spider for spider in BaseSpider.__subclasses__()}
            forms = {form.name: form for form in BaseForm.__subclasses__()}

            for spider in spiders:
                spiders[spider] = {'spider': spiders[spider](), 'form': forms[spider]}

            return spiders
