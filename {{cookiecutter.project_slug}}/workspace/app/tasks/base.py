from abc import ABC
from loguru import logger

import celery


class BaseTask(celery.Task, ABC):
    def on_success(self, retval, task_id, args, kwargs):
        # TODO: Use success logging and maybe add to db
        with logger.contextualize(task_id=task_id):
            logger.debug('Success')

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        # TODO: Add Failure reason and use like finally
        with logger.contextualize(task_id=task_id):
            logger.debug('Failed')
            logger.debug('Error: {}'.format(einfo))

