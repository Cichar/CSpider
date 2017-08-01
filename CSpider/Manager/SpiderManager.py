# -*- coding:utf-8 -*-

from Utils.BaseForm import BaseForm
from Utils.BaseSpider import BaseSpider
from Utils.BaseManager import BaseManager
from Utils.BaseDataAnalysis import BaseDataAnalysis

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/1'
__Version__ = '0.1'


class SpiderManager(BaseManager):
    """ Spider Manager """

    _dir_list = ['Spider', 'Form', 'DataAnalysis']

    def __init__(self):
        super().__init__()
        self._module_import(module_dir=self._dir_list, wrong_file=['__init__'])
        self.spiders = self._create_dict()

    def _create_dict(self):
        """ Create Spiders Dict 
            
            Example:
              {'NetEaseMusicCloud': {'spider': <class 'Spider.NetEaseMusicCloud.NetEaseMusicCloudSpider'>, 
                                     'form': <class 'Form.TaskForm.NetEaseMusicCloudForm'>}, 
               'ZhiHuUser': {'spider': <class 'Spider.Zhihu.ZhiHuSpider'>, 
                             'form': <class 'Form.TaskForm.ZhiHuForm'>}
              }
        """

        spiders = {spider.name: spider for spider in BaseSpider.__subclasses__()}
        forms = {form.name: form for form in BaseForm.__subclasses__()}
        analysis = {_analysis.name: _analysis for _analysis in BaseDataAnalysis.__subclasses__()}

        for spider in spiders:
            spiders[spider] = {'spider': spiders[spider](), 'form': forms.get(spider, None),
                               'analysis': analysis.get(spider, None)}

        return spiders
