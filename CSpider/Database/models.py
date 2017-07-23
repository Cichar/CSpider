# -*- coding:utf-8 -*-

from sqlalchemy import Column, String, Integer, DateTime, TEXT, Boolean

from . import Base


class SpiderTask(Base):
    """ Spider Task Model 
    """

    __tablename__ = 'spiderTask'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), default=u'未知')
    failed = Column(Integer, default=0)
    success = Column(Integer, default=0)
    remain = Column(Integer, default=0)
    status = Column(String(32), default=u'未知')


class ZhiHuUserInfo(Base):
    """ ZhiHu User Info Model
    """

    __tablename__ = 'zhHuUserInfos'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), default=u'未知')
    headline = Column(String(128), default=u'未知')
    location = Column(String(64), default=u'未知')
    description = Column(TEXT(), default=u'未知')
    voteup_count = Column(Integer)
    thanked_count = Column(Integer)
    favorited_count = Column(Integer)
    logs_count = Column(Integer)
    question_count = Column(Integer)
    url_token = Column(String(64), default=u'未知')
    follower_count = Column(Integer)
    following_count = Column(Integer)
    business = Column(String(64), default=u'未知')
    employment = Column(String(64), default=u'未知')
    company = Column(String(64), default=u'未知')
    update_time = Column(DateTime())
    updata_flag = Column(Boolean, default=True)
    crawl_flag = Column(Boolean, default=False)

    def __repr__(self):
        return 'ZhiHuUser %r' % self.name
