# -*- utf-8 -*-

import abc

from Database import db
from Utils.Singleton import ABC

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/8/1'
__Version__ = '0.1'


class BaseDataAnalysis(object, metaclass=ABC):
    _db = None

    @property
    @abc.abstractmethod
    def name(self):
        """ Subclass Need To Provide Name For The BaseDataAnalysis Object """

        return 'BaseDataAnalysis'

    @abc.abstractmethod
    def analysis(self, **kwargs) -> list:
        """ Subclass Need To Return List Object 
            Which Contain Table Object Or Chart Object 
        """

        pass

    @abc.abstractmethod
    def render(self):
        pass

    @property
    def db(self):
        if self._db is None:
            self._db = db
        return self._db

    def query(self, model):
        """ Database Query Function """

        _model = self.db.session.query(model)
        return _model

    def add(self, obj):
        """ Database Add Function """

        self.db.session.add(obj)

    def commit(self):
        """ Database Commit Function """

        self.db.session.commit()
