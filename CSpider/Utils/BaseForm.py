# -*- coding:utf-8 -*-

from wtforms_tornado import Form
from wtforms import widgets
from wtforms.fields import SelectMultipleField

from Database import db


class BaseForm(Form):
    @property
    def db(self):
        return db

    def query(self, model):
        """ 查询数据库 """

        _model = self.db.session.query(model)
        return _model


class MultipleCheckField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()
