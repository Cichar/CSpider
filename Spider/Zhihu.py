# -*- coding:utf-8 -*-

from datetime import datetime

from Utils.BaseSpider import BaseSpider
from Utils.SpiderWorkers import spider_worker
from Database import db
from Database.models import ZhiHuUserInfo

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/1'
__Version__ = '0.1'


class ZhiHuSpider(BaseSpider):
    name = u'ZhiHuUser'

    def __init__(self):
        super().__init__()
        # follower and followed query args
        self.follow_arg = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,' \
                          'is_following,badge[?(type=best_answerer)].topics'
        # user info query args
        self.user_arg = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,' \
                        'following_count,cover_url,following_topic_count,following_question_count,' \
                        'following_favlists_count,following_columns_count,avatar_hue,answer_count,articles_count,' \
                        'pins_count,question_count,commercial_question_count,favorite_count,favorited_count,' \
                        'logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,' \
                        'is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,' \
                        'is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,' \
                        'vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,' \
                        'participated_live_count,allow_message,industry_category,org_name,org_homepage,' \
                        'badge[?(type=best_answerer)].topics'

    def task_distribute(self, data):
        self.start.apply_async(kwargs={'user_token': data['target'], 'updata': False})

    @staticmethod
    @spider_worker.task(rate_limit='10/m')
    def start(user_token=None, updata=False):
        """ ZhiHuSpider Start 
            Start User：tao-zi-de-tao
            
        """

        try:
            if user_token:
                user = db.session.query(ZhiHuUserInfo).filter_by(url_token=user_token).first()
                if not user:
                    spider_worker.send_task('Spider.Zhihu.get_user_infos',
                                            kwargs={'user_token': user_token, 'updata': updata,
                                                    'crawl_flag': True})
            crawl_user = db.session.query(ZhiHuUserInfo).filter_by(crawl_flag=None or False).first()
            while crawl_user:
                crawl_user.crawl_flag = True
                db.session.commit()
                spider_worker.send_task('Spider.Zhihu.get_user_infos',
                                        kwargs={'user_token': crawl_user.url_token, 'updata': updata})
                crawl_user = db.session.query(ZhiHuUserInfo).filter_by(crawl_flag=None or False).first()
        except Exception as err:
            print('** start : %s **' % str(err))

    @staticmethod
    @spider_worker.task(rate_limit='6/m')
    def get_user_infos(user_token=None, updata=False, crawl_flag=False):
        """ Get The User's Info 、 Followers And Following """

        try:
            spider_worker.send_task('Spider.Zhihu.get_user_info',
                                    kwargs={'user_token': user_token, 'updata': updata, 'crawl_flag': crawl_flag},
                                    queue='short_task_1', routing_key='for_short_task_1')
            spider_worker.send_task('Spider.Zhihu.get_user_followers',
                                    kwargs={'user_token': user_token, 'url': None},
                                    queue='long_task_1', routing_key='for_long_task_1')
            spider_worker.send_task('Spider.Zhihu.get_user_following',
                                    kwargs={'user_token': user_token, 'url': None},
                                    queue='long_task_2', routing_key='for_long_task_2')
        except Exception as err:
            print('** get_user_infos : %s **' % str(err))

    @staticmethod
    @spider_worker.task(rate_limit='30/m')
    def get_user_info(user_token=None, updata=False, crawl_flag=False):
        """ Get User Info
            Request URL: http://www.zhihu.com/api/v4/members/{url_token}?include={user_arg}
        """

        user_info_url = 'http://www.zhihu.com/api/v4/members/{url_token}?include={user_arg}'
        try:
            if user_token:
                data = ZhiHuSpider().parse_url(url=user_info_url.format(url_token=user_token,
                                                                        user_arg=ZhiHuSpider().user_arg),
                                               header='zhihu', parse_json=True)
            else:
                data = None
            if data:
                # url_token
                url_token = data.get('url_token')
                if not url_token:
                    print('Invalid User.')
                    return

                name = data['name']
                headline = data.get('headline', '')
                location = data.get('locations', '')
                if location:
                    location = data['locations'][0]['name']
                else:
                    location = ''
                description = data.get('description', '')
                voteup_count = data.get('voteup_count', '')
                thanked_count = data.get('thanked_count', '')
                favorited_count = data.get('favorited_count', '')
                logs_count = data.get('logs_count', '')
                question_count = data.get('question_count', '')
                follower_count = data.get('follower_count', '')
                following_count = data.get('following_count', '')
                business = data.get('business', '')
                if business:
                    business = data['business']['name']

                employment, company = data.get('employments', ''), data.get('employments', '')
                if employment:
                    employment = data['employments'][0].get('company', '')
                    if employment:
                        employment = data['employments'][0]['company']['name']
                else:
                    employment = ''
                if company:
                    company = data['employments'][0].get('job', '')
                    if company:
                        company = data['employments'][0]['job']['name']
                else:
                    company = ''

                user = db.session.query(ZhiHuUserInfo).filter_by(url_token=url_token).first()
                new_user = None
                if updata:
                    if user:
                        user.headline = headline
                        user.location = location
                        user.description = description
                        user.voteup_count = voteup_count
                        user.thanked_count = thanked_count
                        user.favorited_count = favorited_count
                        user.logs_count = logs_count
                        user.question_count = question_count
                        user.follower_count = follower_count
                        user.following_count = following_count
                        user.business = business
                        user.employment = employment
                        user.company = company
                        user.update_time = datetime.utcnow()
                        user.crawl_flag = crawl_flag
                        db.session.commit()
                        print('Update User --> %s' % name)
                        if not user.crawl_flag:
                            spider_worker.send_task('Spider.Zhihu.get_user_infos',
                                                    kwargs={'user_token': url_token, 'updata': True,
                                                            'crawl_flag': True})
                        return
                if not user:
                    new_user = ZhiHuUserInfo(name=name, headline=headline, location=location, description=description,
                                             voteup_count=voteup_count, thanked_count=thanked_count,
                                             favorited_count=favorited_count, logs_count=logs_count,
                                             question_count=question_count, url_token=url_token,
                                             follower_count=follower_count, following_count=following_count,
                                             business=business, employment=employment, company=company,
                                             update_time=datetime.utcnow(), crawl_flag=crawl_flag)
                    db.session.add(new_user)
                    db.session.commit()
                    print('Create User --> %s' % name)
                    if not new_user.crawl_flag:
                        spider_worker.send_task('Spider.Zhihu.get_user_infos',
                                                kwargs={'user_token': url_token, 'updata': True,
                                                        'crawl_flag': True})
            else:
                print('** None User Data Was Obtained **')
            return
        except Exception as err:
            print('** get_user_info : %s **' % str(err))

    @staticmethod
    @spider_worker.task(rate_limit='6/m')
    def get_user_followers(user_token=None, url=None, updata=False):
        """ Get User's Followers
            Request URL: http://www.zhihu.com/api/v4/members/{url_token}/followers?include={follow_arg}&offset={offset}&limit={limit}
        """

        follower_url = 'http://www.zhihu.com/api/v4/members/{url_token}/followers?' \
                       'include={follow_arg}&offset={offset}&limit={limit}'
        try:
            if user_token:
                followers = ZhiHuSpider().parse_url(url=follower_url.format(url_token=user_token,
                                                                            follow_arg=ZhiHuSpider().follow_arg,
                                                    offset=0, limit=20), header='zhihu', parse_json=True)
            else:
                followers = ZhiHuSpider().parse_url(url=url, header='zhihu', parse_json=True)
            if followers:
                if followers.get('data', None):
                    for follower in followers.get('data'):
                        url_token = follower.get('url_token', None)
                        if url_token:
                            user = db.session.query(ZhiHuUserInfo).filter_by(url_token=url_token).first()
                            if updata or not user:
                                spider_worker.send_task('Spider.Zhihu.get_user_info',
                                                        kwargs={'user_token': url_token, 'updata': updata},
                                                        queue='short_task_1', routing_key='for_short_task_1')
                if 'paging' in followers.keys() and followers.get('paging').get('is_end') is False:
                    url = followers.get('paging').get('next')
                    spider_worker.send_task('Spider.Zhihu.get_user_followers',
                                            kwargs={'url': url},
                                            queue='long_task_1', routing_key='for_long_task_1')
        except Exception as err:
            print('** get_user_followers : %s **' % str(err))

    @staticmethod
    @spider_worker.task(rate_limit='6/m')
    def get_user_following(user_token=None, url=None, updata=False):
        """ Get User's Following
            Request URL: https://www.zhihu.com/api/v4/members/{url_token}/followees?include={follow_arg}&offset={offset}&limit={limit}
        """

        following_url = 'http://www.zhihu.com/api/v4/members/{url_token}/followees?' \
                        'include={follow_arg}&offset={offset}&limit={limit}'
        try:
            if user_token:
                followings = ZhiHuSpider().parse_url(url=following_url.format(url_token=user_token,
                                                                              follow_arg=ZhiHuSpider().follow_arg,
                                                     offset=0, limit=20), header='zhihu', parse_json=True)
            else:
                followings = ZhiHuSpider().parse_url(url=url, header='zhihu', parse_json=True)
            if followings:
                if followings.get('data', None):
                    for following in followings.get('data'):
                        url_token = following.get('url_token', None)
                        if url_token:
                            user = db.session.query(ZhiHuUserInfo).filter_by(url_token=url_token).first()
                            if updata or not user:
                                spider_worker.send_task('Spider.Zhihu.get_user_info',
                                                        kwargs={'user_token': url_token, 'updata': updata},
                                                        queue='short_task_1', routing_key='for_short_task_1')
                if 'paging' in followings.keys() and followings.get('paging').get('is_end') is False:
                    url = followings.get('paging').get('next')
                    spider_worker.send_task('Spider.Zhihu.get_user_following',
                                            kwargs={'url': url},
                                            queue='long_task_2', routing_key='for_long_task_2')
        except Exception as err:
            print('** get_user_follow : %s **' % str(err))
