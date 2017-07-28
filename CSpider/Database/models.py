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

    def to_json(self):
        """ Return Json Type """

        _info = {
            'DT_RowId': self.id,
            'id': self.id,
            'name': self.name,
            'failed': self.failed,
            'success': self.success,
            'remain': self.remain,
            'status': self.status,
        }
        return _info


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


class AcFunInfo(Base):
    """ AcFun Info Model
    """

    __tablename__ = 'AcFunInfos'

    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, default=0)
    title = Column(String(192), default=u'未知')
    user_id = Column(Integer, default=0)
    username = Column(String(128), default=u'未知')
    channel = Column(String(128), default=u'未知')
    parent_channel = Column(String(128), default=u'未知')
    view_count = Column(Integer, default=0)
    contribute_time = Column(DateTime())
    comment_count = Column(Integer, default=0)
    dan_mu_size = Column(Integer, default=0)
    banana_count = Column(Integer, default=0)
    favorite_count = Column(Integer, default=0)
    year = Column(Integer, default=0)
    month = Column(Integer, default=0)

    def __repr__(self):
        return 'AcFun Info < %r >' % self.title
