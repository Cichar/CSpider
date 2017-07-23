# -*- utf-8 -*-

from celery import Task

from Database import db


class BaseTask(Task):
    abstract = True
    _db = None

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

    # def __call__(self, *args, **kwargs):
    #     """ Do Additional Thing When Call Task """
    #
    #     print('do something')
    #     return super(BaseTask, self).__call__(*args, **kwargs)

    def send_task(self, name, args=None, kwargs=None, countdown=None,
                  eta=None, task_id=None, producer=None, connection=None,
                  router=None, result_cls=None, expires=None,
                  publisher=None, link=None, link_error=None,
                  add_to_parent=True, group_id=None, retries=0, chord=None,
                  reply_to=None, time_limit=None, soft_time_limit=None,
                  root_id=None, parent_id=None, route_name=None,
                  shadow=None, chain=None, task_type=None, **options):
        """ Do Additional Thing, Then Send Task """

        st_id = kwargs.get('st_id', None)

        if st_id:
            self.app.send_task('CommonTask.task_update.task_info_update',
                               kwargs={'st_id': st_id, 'event': 'remain'},
                               queue='common_task_1', routing_key='for_common_task_1')

        self.app.send_task(name, args=args, kwargs=kwargs, countdown=countdown,
                           eta=eta, task_id=task_id, producer=producer, connection=connection,
                           router=router, result_cls=result_cls, expires=expires,
                           publisher=publisher, link=link, link_error=link_error,
                           add_to_parent=add_to_parent, group_id=group_id, retries=retries, chord=chord,
                           reply_to=reply_to, time_limit=time_limit, soft_time_limit=soft_time_limit,
                           root_id=root_id, parent_id=parent_id, route_name=route_name,
                           shadow=shadow, chain=chain, task_type=task_type, **options)

    def run(self, *args, **kwargs):
        pass

    def on_failure(self, exc, task_id, args, kwargs, info):
        """ Do Additional Thing When Task Failed """

        print(str(exc), task_id, args, kwargs, info)
        st_id = kwargs.get('st_id', None)
        if st_id:
            self.app.send_task('CommonTask.task_update.task_info_update',
                               kwargs={'st_id': st_id, 'event': 'failed'},
                               queue='common_task_1', routing_key='for_common_task_1')

    def on_success(self, ret_val, task_id, args, kwargs):
        """ Do Additional Thing When Task Success """

        st_id = kwargs.get('st_id', None)
        if st_id:
            self.app.send_task('CommonTask.task_update.task_info_update',
                               kwargs={'st_id': st_id, 'event': 'success'},
                               queue='common_task_1', routing_key='for_common_task_1')


class CommonTask(BaseTask):
    def send_task(self, name, args=None, kwargs=None, countdown=None,
                  eta=None, task_id=None, producer=None, connection=None,
                  router=None, result_cls=None, expires=None,
                  publisher=None, link=None, link_error=None,
                  add_to_parent=True, group_id=None, retries=0, chord=None,
                  reply_to=None, time_limit=None, soft_time_limit=None,
                  root_id=None, parent_id=None, route_name=None,
                  shadow=None, chain=None, task_type=None, **options):
        pass

    def on_success(self, ret_val, task_id, args, kwargs):
        pass
