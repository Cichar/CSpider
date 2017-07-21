# -*- utf-8 -*-

import numbers

try:
    from urllib.parse import unquote
    from urllib.parse import urlparse
except:
    from urlparse import urlparse
    from urllib2 import unquote


class BrokerBase(object):
    def __init__(self, broker_url, *args, **kwargs):
        """ 
            Example:
                broker_url = 'redis://localhost:6379/1'
                purl = ParseResult(scheme='redis', netloc='localhost:6379', path='/1', params='', query='', fragment='')
        """
        purl = urlparse(broker_url)
        self.host = purl.hostname
        self.port = purl.port
        self.db_info = purl.path

        username = purl.username
        password = purl.password

        self.username = unquote(username) if username else username
        self.password = unquote(password) if password else password

    def queues(self, names):
        raise NotImplementedError


class Redis(BrokerBase):
    sep = '\x06\x16'
    DEFAULT_PRIORITY_STEPS = [0, 3, 6, 9]

    def __init__(self, broker_url, *args, **kwargs):
        super(Redis, self).__init__(broker_url)
        self.host = self.host or 'localhost'
        self.port = self.port or 6379
        self.db_num = self._prepare_db_num(self.db_info)

        try:
            import redis
        except Exception:
            raise ImportError('redis library is required')

        self.redis = redis.Redis(host=self.host, port=self.port, db=self.db_num, password=self.password)

        broker_options = kwargs.get('broker_options')

        # There are 10(0-9) priority level in celery, 4 levels by default. such as [0, 3, 6 ,9]
        # If want more priority level, user can set ''priority_steps'' transport option
        # Example:
        # BROKER_TRANSPORT_OPTIONS = {'priority_steps': list(range(10))}
        if broker_options and 'priority_steps' in broker_options:
            self.priority_steps = broker_options['priority_steps']
        else:
            self.priority_steps = self.DEFAULT_PRIORITY_STEPS

    def _str_for_priority(self, queue, priority):
        """ Return Format String For redis.llen()
            Example:
                'default'
                'default\x06\x163'
                'default\x06\x166'
                'default\x06\x169'  
        """

        if priority not in self.priority_steps:
            raise ValueError('Priority: {0} not in priority steps'.format(priority))
        return '{0}{1}{2}'.format(*((queue, self.sep, priority) if priority else (queue, '', '')))

    def queues(self, names):
        """ Get The Redis Queues Infos 
            Example:
                [{'name': 'default', 'messages': 57372}]
        """

        queue_stats = []
        for name in names:
            priority_names = [self._str_for_priority(name, priority) for priority in self.priority_steps]
            queue_stats.append({
                'name': name,
                'messages': sum([self.redis.llen(x) for x in priority_names])
            })
        return queue_stats

    @staticmethod
    def _prepare_db_num(db_info):
        """ Parse And Return The Redis Database Num """

        db_num = 0
        if not isinstance(db_info, numbers.Integral):
            if not db_info or db_info == '/':
                db_num = db_num
            elif db_info.startswith('/'):
                db_num = db_info[1:]
            try:
                db_num = int(db_num)
            except ValueError:
                raise ValueError(
                    "Redis Database is integer between 0 and limit - 1, not {0}".format(db_num)
                )
        return db_num


class Broker(object):
    def __new__(cls, broker_url, *args, **kwargs):
        scheme = urlparse(broker_url).scheme
        if scheme == 'redis':
            return Redis(broker_url, *args, **kwargs)
        else:
            raise NotImplementedError
