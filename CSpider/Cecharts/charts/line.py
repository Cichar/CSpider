# -*- utf-8 -*-

from Cecharts.BaseChart import BaseChart


class LineChart(BaseChart):
    def update_series(self, datas, legend=True):
        if not datas or not isinstance(datas, dict):
            raise ValueError('datas is required and must be dict type. such as {"name": [14, 52, 32, 52]}')
        if legend:
            self._update_legend(list(datas.keys()))
        for k, v in datas.items():
            if not isinstance(k, str):
                raise ValueError('name must be string type, get {0} type'.format(type(k).__name__))
            if not isinstance(v, list):
                raise ValueError('data must be list type, get {0} type'.format(type(v).__name__))
            self._option['series'].append({
                'name': k,
                'type': 'line',
                'data': v
            })
