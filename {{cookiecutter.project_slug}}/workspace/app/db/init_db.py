from app import crud
from app.core import config
from app.schemas.user import UserCreate


def init_db(db_session):
    user = crud.user.get_by_email(db_session, email=config.SUPERUSER_EMAIL)
    if not user:
        user_in = UserCreate(
            full_name=config.SUPERUSER_FULL_NAME,
            email=config.SUPERUSER_EMAIL,
            password=config.SUPERUSER_PASSWORD,
            webhook_url=config.SUPERUSER_WEBHOOK,
            is_superuser=True
        )
        user = crud.user.create(db_session, obj_in=user_in)
