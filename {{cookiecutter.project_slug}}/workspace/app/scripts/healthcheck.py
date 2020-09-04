from typing import Optional, Union

import pika
from loguru import logger

from app.core.celeryconfig import broker_url
from app.db.session import db_session


def db_healthcheck() -> Union[bool, Optional[Exception]]:
    try:
        db_session.execute("SELECT 1")
        logger.success("DB Connection Successful")
        return True, None
    except Exception as e:
        logger.error(e)
        return False, e


def broker_healthcheck() -> Union[bool, Optional[Exception]]:
    parameters = pika.URLParameters(broker_url)
    try:
        connection = pika.BlockingConnection(parameters)
        assert connection.is_open
        connection.close()
        logger.success("Broker Connection Successful")
        return True, None
    except AssertionError as e:
        logger.error("Broker Connection Failed")
        return False, e
    except Exception as e:
        logger.error(e)
        return False, e
