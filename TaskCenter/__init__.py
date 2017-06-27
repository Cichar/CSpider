# -*- coding:utf-8 -*-

from celery import Celery

from Conf.config import CELERY_BROKER_URI


celery_app = Celery('spider_task', broker=CELERY_BROKER_URI)

celery_app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
)
