# -*- coding:utf-8 -*-

from tornado import gen

from Utils.BaseHandle import BaseHandler

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/1'
__Version__ = '0.1'


class DataAnalysisHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        analysis = [_analysis for _analysis in self.spiders if self.spiders[_analysis]['analysis']]
        return self.render("data_analysis.html", analysis=analysis)


class AnalysisRenderHandler(BaseHandler):
    @gen.coroutine
    def get(self, spider_name):
        render = self.spiders[spider_name]['analysis']().render()
        return self.render("analysis_render.html", render=render)


class AnalysisReportHandler(BaseHandler):
    @gen.coroutine
    def get(self, spider_name):
        data = self.clear_args(self.request.arguments)
        renders = self.spiders[spider_name]['analysis']().analysis(**data)
        return self.render("analysis_report.html", renders=renders)
