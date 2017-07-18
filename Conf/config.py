# -*- coding:utf-8 -*-

from collections import defaultdict


class DefaultConfig(object):
    # Celery Monitor Configuration
    MONITOR_EVENTS_ENABLE_INTERVAL = 5000
    MONITOR_UPDATE_INTERVAL = 3000


class DevelopmentConfig(DefaultConfig):
    # Database URI
    SQLALCHEMY_DATABASE_URI = ''

    # Celery broker
    CELERY_BROKER_URI = 'redis://localhost:6379/1'


class TestingConfig(DefaultConfig):
    # Database URI
    SQLALCHEMY_DATABASE_URI = ''

    # Celery broker
    CELERY_BROKER_URI = 'redis://'


class ProductionConfig(DefaultConfig):
    # Database URI
    SQLALCHEMY_DATABASE_URI = ''

    # Celery broker
    CELERY_BROKER_URI = 'redis://'


def config_from_object(obj):
    """ Updates The Extra Configuration From The Given Object """

    _config = defaultdict(dict)
    for key in dir(obj):
        if key.isupper():
            if key.startswith('MONITOR_'):
                _config['MONITOR'][key] = getattr(obj, key)
            else:
                _config[key] = getattr(obj, key)
    return _config

config = {
    'development': config_from_object(DevelopmentConfig),
    'testing': config_from_object(TestingConfig),
    'production': config_from_object(ProductionConfig),
    'default': config_from_object(DevelopmentConfig)
}
