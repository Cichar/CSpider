# -*- coding:utf-8 -*-

from wtforms.validators import DataRequired
from wtforms.fields import StringField, SubmitField, SelectField

from Utils.BaseForm import BaseForm
from Utils.BaseForm import MultipleCheckField


class ZhiHuForm(BaseForm):
    """ ZhiHu Spider Task Form """
    name = u'ZhiHuUser'

    target = StringField('Start Target', validators=[DataRequired()])
    submit = SubmitField('Submit')


class NetEaseMusicCloudForm(BaseForm):
    """ NetEaseMusicCloud Task Form """
    name = u'NetEaseMusicCloud'

    module = SelectField('Module', validators=[DataRequired()], coerce=str)
    music_style = MultipleCheckField('Styles', validators=[DataRequired()], coerce=str)
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(NetEaseMusicCloudForm, self).__init__(*args, **kwargs)
        self.module.choices = [('MusicList', 'MusicList'), ('Music', 'Music'), ('Mixed Module', 'Mixed Module')]
        self.music_style.choices = [('LightMusic', 'Light Music'), ('Electronic Music', 'Electronic Music'),
                                    ('ACG Music', 'ACG Music'), ('Healing Music', 'Healing Music')]
