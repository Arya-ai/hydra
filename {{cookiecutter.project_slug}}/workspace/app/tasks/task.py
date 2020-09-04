from time import sleep
from loguru import logger

from .celery import app
from .base import BaseTask

@app.task(base=BaseTask, name='sample.sleep_task_no_result', bind=True)
def celery_sleep_task_no_result(self, number: int):
    """A sample celery task which uses sleep

    Args:
        number (int): Number of seconds to sleep
    """
    task_id = self.request.id
    with logger.contextualize(task_id=task_id):
        try:
            logger.info('Starting Sleep')
            sleep(number)
            logger.info('Ending Sleep')
        except Exception as e:
            logger.error(e)


@app.task(base=BaseTask, name='sample.sleep_task_with_result', bind=True)
def celery_sleep_task_with_result(self, number: int):
    """A sample celery task which uses sleep and returns a result

    Args:
        number (int): Number of seconds to sleep
    """
    task_id = self.request.id
    with logger.contextualize(task_id=task_id):
        try:
            logger.info('Starting Sleep')
            sleep(number)
            logger.info('Ending Sleep')
            return number**2
        except Exception as e:
            logger.error(e)
