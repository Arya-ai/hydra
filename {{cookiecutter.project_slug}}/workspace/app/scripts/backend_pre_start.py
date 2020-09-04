import pika
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_fixed

from app.utils.tenacity import custom_before_log, custom_after_log

from app.scripts.healthcheck import db_healthcheck, broker_healthcheck

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=custom_before_log('Test DB Connection', logger, logger.level("DEBUG")),
    after=custom_after_log('Test DB Connection', logger, logger.level("WARNING"))
)
def test_db_connection():
    status, err = db_healthcheck()
    if not status:
        raise err


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=custom_before_log('Test RabbitMQ Connection', logger, logger.level("DEBUG")),
    after=custom_after_log('Test RabbitMQ Connection', logger, logger.level("WARNING"))
)
def test_queue_connection():
    status, err = broker_healthcheck()
    if not status:
        raise err


def init():
    test_db_connection()
    test_queue_connection()


def main():
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
