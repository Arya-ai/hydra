import os
from multiprocessing import cpu_count

from kombu import Queue


broker_url = 'amqp://{user}:{password}@{host}:{port}/{vhost}'.format(
    user=os.environ.get('BROKER_USER', os.environ.get('ENV_BROKER_USER', 'arya')),
    password=os.environ.get('BROKER_PASSWORD', os.environ.get('ENV_BROKER_PASSWORD', 'changethis')),
    host=os.environ.get('BROKER_HOST', os.environ.get('ENV_BROKER_HOST', 'localhost')),
    port=os.environ.get('BROKER_PORT', os.environ.get('ENV_BROKER_PORT', '5672')),
    vhost=os.environ.get('BROKER_VHOST', os.environ.get('ENV_BROKER_VHOST', 'arya_vhost'))
)

accept_content = ['json', 'msgpack']
result_serializer = 'msgpack'
task_serializer = 'msgpack'

result_backend = 'db+postgresql://{user}:{password}@{host}:{port}/{db}'.format(
    user=os.environ.get('BACKEND_USER', os.environ.get('ENV_BACKEND_USER', 'arya')),
    password=os.environ.get('BACKEND_PASSWORD', os.environ.get('ENV_BACKEND_PASSWORD', 'changethis')),
    host=os.environ.get('BACKEND_HOST', os.environ.get('ENV_BACKEND_HOST', 'localhost')),
    port=os.environ.get('BACKEND_PORT', os.environ.get('ENV_BACKEND_PORT', '5432')),
    db=os.environ.get('BACKEND_DB', os.environ.get('ENV_BACKEND_DB', 'arya_db'))
)

worker_concurrency = max(int(1.5 * cpu_count()), 8)
worker_hijack_root_logger = False
worker_log_color = False

task_always_eager = False
task_acks_late = True
task_soft_time_limit = 60 * 3  # 3 minutes


timezone = 'Asia/Kolkata'

task_default_queue = 'celery'

task_queues = (
    Queue('sample', routing_key='sample'),
)

imports = (
    'app.tasks.task'
)

task_routes = {
    'sample.sleep_task_no_result': {
        'queue': 'sample'
    },
    'sample.sleep_task_with_result': {
        'queue': 'sample'
    }
}
