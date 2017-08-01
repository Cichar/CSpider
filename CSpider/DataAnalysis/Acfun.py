# -*- utf-8 -*-

from Spider.Acfun import AcFunSpider
from Database.models import AcFunInfo
from Htmlrender.Ctable.Table import Table
from Utils.BaseDataAnalysis import BaseDataAnalysis


class AcFunAnalysis(BaseDataAnalysis):
    name = u'AcFun'

    def render(self):
        _years = self.query(AcFunInfo.year.distinct().label('year')).all()
        _months = self.query(AcFunInfo.month.distinct().label('month')).all()
        years = sorted([data.year for data in _years])
        months = sorted([data.month for data in _months])
        dates = []
        for year in years:
            for month in months:
                if self.query(AcFunInfo).filter_by(year=year, month=month).first():
                    dates.append((year, month))

        table = Table(head=['时间', '链接'],
                      body=[('{0}年{1}月'.format(data[0], data[1]),
                             '<a href="/analysis_report/{name}?year={year}&month={month}">数据</a>'.format(
                                 name=self.name, year=data[0], month=data[1])) for data in dates]).render()
        return table

    def analysis(self, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')

        datas = [data for data in self.query(AcFunInfo).filter_by(year=int(year), month=int(month)).all()]

        # 7月得蕉 TOP50 视频
        banana_source_top_50 = self.query(AcFunInfo).filter_by(year=int(year), month=int(month)).order_by(
            AcFunInfo.banana_count.desc()).offset(0).limit(50).all()

        # 7月收藏 TOP50 视频
        favorite_count_top_50 = self.query(AcFunInfo).filter_by(year=int(year), month=int(month)).order_by(
            AcFunInfo.favorite_count.desc()).offset(0).limit(50).all()

        # 7月总投稿数
        source_num = len(datas)
        # 7月投稿的UP数
        up_user = set()
        # 7月总播放量、总蕉数
        view_num = banana_num = 0
        # Up 收视TOP50， Up 香蕉TOP50，Up 投稿TOP50, 收藏TOP50 各分区投稿数与播放量
        view_up_top_50 = {}
        banana_up_top_50 = {}
        source_up_top_50 = {}
        favorite_top_50 = {}
        channel_dict = {}

        # 生成默认的分区字典
        for key in AcFunSpider.CHANNEL_LIST.keys():
            channel_dict[key] = {}
            for k in AcFunSpider.CHANNEL_LIST[key]:
                channel_dict[key].update({k['name']: {'source_count': 0, 'view_count': 0}})

        for data in datas:
            # 更新投稿UP
            up_user.add(data.user_id)

            # 统计总播放量及香蕉数
            view_num += data.view_count
            banana_num += data.banana_count

            # 更新分区字典数据
            channel_dict[data.parent_channel][data.channel]['source_count'] += 1
            channel_dict[data.parent_channel][data.channel]['view_count'] += data.view_count

            # 更新Up 收视TOP50
            if not view_up_top_50.get(data.username, None):
                view_up_top_50[data.username] = 0
            view_up_top_50[data.username] += data.view_count

            # 更新Up 香蕉TOP50
            if not banana_up_top_50.get(data.username, None):
                banana_up_top_50[data.username] = 0
            banana_up_top_50[data.username] += data.banana_count

            # 更新Up 投稿TOP50
            if not source_up_top_50.get(data.username, None):
                source_up_top_50[data.username] = 0
            source_up_top_50[data.username] += 1

            # 更新 收藏TOP50
            if not favorite_top_50.get(data.username, None):
                favorite_top_50[data.username] = 0
            favorite_top_50[data.username] += data.favorite_count

        # 生成汇总信息
        infos_table = Table(title='ACFUN {0}年{1}月整体数据'.format(int(year), int(month)),
                            head=['时间', '总投稿', '投稿UP', '人均投稿', '总点击(包括文章区)',
                                  '稿件平均点击', '总蕉数', 'UP人均得蕉'],
                            body=[('{0}月'.format(int(month)), source_num, len(up_user), source_num // len(up_user),
                                   view_num, view_num // source_num, banana_num, banana_num // len(up_user))]).render()

        # 生成分区信息
        channel_data = []
        for _, datas in channel_dict.items():
            for k, v in datas.items():
                channel_data.append((k, v['source_count'], v['view_count']))

        channel_table = Table(title='{0}月各分区稿件及收视'.format(int(month)),
                              head=['分类', '稿件数', '收视'],
                              body=channel_data).render()

        # 生成Up 收视TOP50
        view_up_top_50 = Table(title='{0}月UP收视TOP50'.format(int(month)), title_size='15px',
                               head=['UP', u'收视'],
                               body=sorted(view_up_top_50.items(), key=lambda item: item[1], reverse=True)[:50],
                               _class='col-md-3').render()

        # 生成Up 香蕉TOP50
        banana_up_top_50 = Table(title='{0}月UP得蕉TOP50'.format(int(month)), title_size='15px',
                                 head=['UP', u'得蕉'],
                                 body=sorted(banana_up_top_50.items(), key=lambda item: item[1], reverse=True)[:50],
                                 _class='col-md-3').render()

        # 生成Up 投稿TOP50
        source_up_top_50 = Table(title='{0}月UP投稿TOP50'.format(int(month)), title_size='15px',
                                 head=['UP', u'投稿'],
                                 body=sorted(source_up_top_50.items(), key=lambda item: item[1], reverse=True)[:50],
                                 _class='col-md-3').render()

        # 生成Up 投稿被收藏TOP50
        favorite_top_50 = Table(title='{0}月UP稿件被收藏TOP50'.format(int(month)), title_size='15px',
                                head=['UP', u'获得收藏'],
                                body=sorted(favorite_top_50.items(), key=lambda item: item[1], reverse=True)[:50],
                                _class='col-md-3').render()

        # 生成整月香蕉TOP50
        banana_source_top_50 = Table(title='{0}月香蕉TOP50'.format(int(month)),
                                     head=['UP', '稿件名', '香蕉'],
                                     body=[(data.username, data.title, data.banana_count)
                                           for data in banana_source_top_50]).render()

        # 生成整月收藏TOP50
        favorite_count_top_50 = Table(title='{0}月收藏TOP50'.format(int(month)),
                                      head=['UP', '稿件名', '收藏'],
                                      body=[(data.username, data.title, data.favorite_count)
                                            for data in favorite_count_top_50]).render()

        renders = [infos_table,
                   channel_table,
                   view_up_top_50,
                   banana_up_top_50,
                   source_up_top_50,
                   favorite_top_50,
                   banana_source_top_50,
                   favorite_count_top_50]

        return renders
