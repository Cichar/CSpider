start celery -A Utils.SpiderWorkers worker -l warning -c 1 -Q default
start celery -A Utils.SpiderWorkers worker -l warning -c 1 -Q short_task_1
start celery -A Utils.SpiderWorkers worker -l warning -c 1 -Q long_task_1
start celery -A Utils.SpiderWorkers worker -l warning -c 1 -Q long_task_2