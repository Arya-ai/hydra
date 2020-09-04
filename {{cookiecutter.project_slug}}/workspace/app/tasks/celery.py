from __future__ import absolute_import, unicode_literals

import sys

from celery import Celery
from loguru import logger

from app.core.config import CELERY_APP_NAME
from .config import IS_WORKER, LOG_LEVEL


WORKER_LOGGER_FORMAT = "<green>{time:YYYY-MM-DD at HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{extra[" \
                       "task_id]}</cyan> - <level>{message}</level> "

WORKER_LOGGER_CONFIG = {
    'handlers': [
        {'sink': sys.stdout, 'format': WORKER_LOGGER_FORMAT, 'level': LOG_LEVEL}
    ]
}


def setup_worker_logger():
    if IS_WORKER:
        logger.configure(**WORKER_LOGGER_CONFIG)


app = Celery(CELERY_APP_NAME)
app.config_from_object('app.core.celeryconfig')
app.conf.humanize(with_defaults=True, censored=True)
setup_worker_logger()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
