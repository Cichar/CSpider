# -*- coding:utf-8 -*-

from celery import Celery
from kombu import Queue
from kombu import Exchange

from Conf.config import config

spider_worker = Celery('CSpider', include=['Spider', 'CommonTask'], broker=config['default']['CELERY_BROKER_URI'],
                       task_cls='Utils.BaseTask.BaseTask')

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
    # Default Task Configuration
    CELERY_DEFAULT_QUEUE='default',
    CELERY_DEFAULT_EXCHANGE='default',
    CELERY_DEFAULT_ROUTING_KEY='for_default',
    # Task Queue
    CELERY_QUEUES=(
        Queue("default", Exchange("default", type='direct'), routing_key="for_default"),
        Queue("common_task_1", Exchange("common_task_1", type='direct'), routing_key="for_common_task_1"),
        Queue("long_task_1", Exchange("long_task_1", type='direct'), routing_key="for_long_task_1"),
        Queue("long_task_2", Exchange("long_task_2", type='direct'), routing_key="for_long_task_2"),
        Queue("long_task_3", Exchange("long_task_3", type='direct'), routing_key="for_long_task_3"),
        Queue("long_task_4", Exchange("long_task_4", type='direct'), routing_key="for_long_task_4"),
        Queue("short_task_1", Exchange("short_task_1", type='direct'), routing_key="for_short_task_1"),
        Queue("short_task_2", Exchange("short_task_2", type='direct'), routing_key="for_short_task_2"),
        Queue("short_task_3", Exchange("short_task_3", type='direct'), routing_key="for_short_task_3"),
        Queue("short_task_4", Exchange("short_task_4", type='direct'), routing_key="for_short_task_4"),
    ),
    # Task Route
    CELERY_ROUTES={
        'default': {'queue': 'default', 'routing_key': 'for_default'},
    }
)
