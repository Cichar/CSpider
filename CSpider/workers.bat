start celery -A Utils.SpiderWorkers worker -l warning -c 1 -Q default --hostname default_host
start celery -A Utils.SpiderWorkers worker -l warning -c 1 -Q short_task_1 --hostname short_host_1
start celery -A Utils.SpiderWorkers worker -l warning -c 1 -Q long_task_1 --hostname long_host_1
start celery -A Utils.SpiderWorkers worker -l warning -c 1 -Q long_task_2 --hostname long_host_2
start celery -A Utils.SpiderWorkers worker -l warning -c 1 -Q common_task_1 --hostname common_host_1