# -*- coding:utf-8 -*-

from celery import Celery
from kombu import Queue
from kombu import Exchange

from Conf.config import CELERY_BROKER_URI


spider_worker = Celery('CSpider', include=['Spider'], broker=CELERY_BROKER_URI)

spider_worker.conf.update(
    # TimeZone
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    # Serializer
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    # Schedule Task
    # cmd: celery beat -A Utils.SpiderWorkers -l info
    CELERYBEAT_SCHEDULE={
        'test_task': {
            'task': 'Spider.Zhihu.add',
            'schedule': 60,
            'args': ('23',),
        },
    },
    # Task Queue
    CELERY_QUEUES={
        Queue("default", Exchange("default", type='direct'), routing_key="for_default"),
    },
    # Default Task Configuration
    CELERY_DEFAULT_QUEUE='default',
    CELERY_DEFAULT_EXCHANGE='default',
    CELERY_DEFAULT_ROUTING_KEY='for_default',
    # Task Rounte
    CELERY_ROUTES = {
        '': {'queue': 'default', 'routing_key': 'for_default'},
    }
)
