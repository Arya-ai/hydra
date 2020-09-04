from loguru import logger

from app.db.init_db import init_db
from app.db.session import db_session


def init():
    init_db(db_session)


def main():
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
