# -*- coding:utf-8 -*-

from wtforms.validators import DataRequired
from wtforms.fields import StringField, SubmitField, SelectField

from Utils.BaseForm import BaseForm


class ZhiHuForm(BaseForm):
    """ ZhiHu Spider Task Form """
    name = u'ZhiHuUser'

    target = StringField('start target', validators=[DataRequired()])
    submit = SubmitField('Submit')


class NetEaseMusicCloudForm(BaseForm):
    """ NetEaseMusicCloud Task Form """
    name = u'NetEaseMusicCloud'
