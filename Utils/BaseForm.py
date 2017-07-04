# -*- coding:utf-8 -*-

from wtforms_tornado import Form

from Database import db


class BaseForm(Form):
    @property
    def db(self):
        return db

    def query(self, model):
        """ 查询数据库 """

        _model = self.db.session.query(model)
        return _model
