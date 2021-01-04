from loguru import logger

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app.utils.tenacity import custom_before_log, custom_after_log
from app.db.session import Session as SessionLocal

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1

@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=custom_before_log('Unit Testing', logger, logger.level("INFO")),
    after=custom_after_log('Unit Testing', logger, logger.level("WARNING"))
)
def init() -> None:
    try:
        # Try to create session to check if DB is awake
        db = SessionLocal()
        db.execute("SELECT 1")
        logger.success("Backend Services Connected")
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
