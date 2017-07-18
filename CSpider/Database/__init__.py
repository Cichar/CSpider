# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from Conf.config import config

Base = declarative_base()


class DataBase:
    """

    完成对数据库的连接及操作，提供session实例

    """

    def __init__(self):
        self.metadata = Base.metadata
        self.engine = self.create_the_engine()
        self.session = self.create_session()

    @staticmethod
    def create_the_engine():
        """

        创建数据库连接

        """

        created_engine = create_engine(config['default']['SQLALCHEMY_DATABASE_URI'] + '?charset=utf8',
                                       encoding='utf-8', pool_recycle=5, pool_size=20)
        return created_engine

    def init_db(self):
        """

        在数据库中创建表

        """

        self.metadata.create_all(self.engine)

    def create_session(self):
        """

        创建session实例

        """

        create_session = sessionmaker(bind=self.engine)
        created_session = create_session()
        return created_session

db = DataBase()
