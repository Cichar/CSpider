# -*- utf-8 -*-

from Database.models import AcFunInfo
from Utils.BaseSpider import BaseSpider
from Utils.SpiderWorkers import spider_worker

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/26'
__Version__ = '0.1'


class AcFunSpider(BaseSpider):
    name = u'AcFun'

    API_URL = 'http://www.acfun.cn/list/getlist?channelId={0}&sort=0&pageSize=20&pageNo='
    CHANNEL_LIST = {
        u'动画': [
            {'id': 159, 'name': u'动画资讯'},
            {'id': 109, 'name': u'旧番补档'},
            {'id': 67, 'name': u'新番连载'},
            {'id': 107, 'name': u'MAD·AMV'},
            {'id': 108, 'name': u'MMD·3D'},
            {'id': 133, 'name': u'2.5次元'},
            {'id': 120, 'name': u'国产动画'},
        ], u'音乐': [
            {'id': 136, 'name': u'原创·翻唱'},
            {'id': 137, 'name': u'演奏'},
            {'id': 103, 'name': u'Vocaloid'},
            {'id': 138, 'name': u'日系音乐'},
            {'id': 139, 'name': u'综合音乐'},
            {'id': 140, 'name': u'演唱会'},
        ], u'舞蹈·彼女': [
            {'id': 134, 'name': u'宅舞'},
            {'id': 135, 'name': u'综合舞蹈'},
            {'id': 129, 'name': u'爱豆'},
            {'id': 130, 'name': u'手作'},
            {'id': 127, 'name': u'造型'},
        ], u'游戏': [
            {'id': 84, 'name': u'主机单机'},
            {'id': 83, 'name': u'游戏集锦'},
            {'id': 145, 'name': u'电子竞技'},
            {'id': 85, 'name': u'英雄联盟'},
            {'id': 170, 'name': u'守望先锋'},
            {'id': 165, 'name': u'桌游卡牌'},
            {'id': 72, 'name': u'Mugen'},
        ], u'娱乐': [
            {'id': 86, 'name': u'生活娱乐'},
            {'id': 87, 'name': u'鬼畜调教'},
            {'id': 88, 'name': u'萌宠'},
            {'id': 89, 'name': u'美食'},
            {'id': 98, 'name': u'综艺'},
        ], u'科技': [
            {'id': 90, 'name': u'科学技术'},
            {'id': 151, 'name': u'教程'},
            {'id': 91, 'name': u'数码'},
            {'id': 122, 'name': u'汽车'},
            {'id': 149, 'name': u'广告'},
        ],
        u'体育': [
            {'id': 152, 'name': u'综合体育'},
            {'id': 94, 'name': u'足球'},
            {'id': 95, 'name': u'篮球'},
            {'id': 153, 'name': u'搏击'},
            {'id': 154, 'name': u'11区体育'},
            {'id': 93, 'name': u'惊奇体育'},
        ], u'鱼塘': [
            {'id': 131, 'name': u'历史'},
        ], u'文章': [
            {'id': 110, 'name': u'综合'},
            {'id': 73, 'name': u'工作·情感'},
            {'id': 74, 'name': u'动漫文化'},
            {'id': 75, 'name': u'漫画·轻小说'},
            {'id': 164, 'name': u'游戏'},
        ],
    }

    def task_distribute(self, data, st_id=None):
        self.start.apply_async(kwargs={'data': data, 'st_id': st_id},
                               queue='short_task_2', routing_key='for_short_task_2')

    @staticmethod
    @spider_worker.task(bind=True, rate_limit='15/m')
    def start(base, data=None, st_id=None):
        if data['month'] < 10:
            month = '0%d' % data['month']
        else:
            month = data['month']
        for parent_channel, channels in AcFunSpider().CHANNEL_LIST.items():
            for channel in channels:
                channel_url = AcFunSpider().API_URL.format(channel['id'])
                base.send_task('Spider.Acfun.get_info',
                               kwargs={'parent_channel': parent_channel, 'channel_url': channel_url,
                                       'page': 1, 'channel_name': channel['name'], 'year': data['year'],
                                       'month': month, 'st_id': st_id},
                               queue='short_task_2', routing_key='for_short_task_2')

    @staticmethod
    @spider_worker.task(bind=True, rate_limit='15/m')
    def get_info(base, parent_channel=None, channel_url=None, page=None,
                 channel_name=None, year=None, month=None, st_id=None):
        try:
            url = channel_url + str(page)
            datas = AcFunSpider().parse_url(url=url, header='default', parse_json=True)
            for index, data in enumerate(datas['data']['data']):
                if data['contributeTimeFormat'] >= '{0}-{1}-01 00:00:00'.format(year, month):
                    new_source = AcFunInfo(source_id=data['id'], title=data['title'], user_id=data['userId'],
                                           username=data['username'], channel=channel_name,
                                           parent_channel=parent_channel, view_count=data['viewCount'],
                                           contribute_time=data['contributeTimeFormat'],
                                           comment_count=data['commentCount'], dan_mu_size=data['danmuSize'],
                                           banana_count=data['bananaCount'], favorite_count=data['favoriteCount'],
                                           year=int(year), month=int(month))
                    base.add(new_source)
                    base.commit()
                    if index == len(datas) - 1:
                        page += 1
                        base.send_task('Spider.Acfun.get_info',
                                       kwargs={'parent_channel': parent_channel, 'channel_url': channel_url,
                                               'page': page, 'channel_name': channel_name, 'year': year,
                                               'month': month, 'st_id': st_id},
                                       queue='short_task_2', routing_key='for_short_task_2')
        except Exception as err:
            raise err
