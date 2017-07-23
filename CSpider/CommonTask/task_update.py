# -*- utf-8 -*-

from Database.models import SpiderTask
from Utils.BaseTask import CommonTask
from Utils.SpiderWorkers import spider_worker


@spider_worker.task(bind=True, base=CommonTask)
def task_info_update(base, st_id=None, event=None):
    """ This Common Task Is Use To Update Spider Task Info In Database """

    task = None
    try:
        if st_id:
            task = base.query(SpiderTask).filter_by(id=int(st_id)).first()
            task.status = 'running'
        if task and event == 'remain':
            task.remain += 1
        elif task and event == 'success':
            task.remain -= 1
            task.success += 1
        elif task and event == 'failed':
            task.remain -= 1
            task.failed += 1
        else:
            pass
    except Exception as err:
        print(str(err))
    else:
        if event != 'remain':
            print('Task %s Done' % event)
        base.commit()
