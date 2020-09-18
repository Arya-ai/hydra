import base64
import os

# Utility Methods
import sys


def get_env_boolean(var_name: str, default: bool = False):
    result = default
    env_value = os.getenv(var_name, None)
    if env_value:
        result = env_value.upper() in ("TRUE", "1")
    return result


# Template Specific
ENV = os.getenv('ENV', 'local').lower()
IS_PROD = ENV == 'production'

API_V1_STR = "/api/v1"
OPENAPI_URL = os.path.join(API_V1_STR, 'openapi.json')

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days
SECRET_KEY = os.getenv('SECRET_KEY')

# Database Settings
POSTGRES_SERVER = os.getenv('POSTGRES_SERVER')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')

SQLALCHEMY_DATABASE_URI = (
    f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}'
)

SUPERUSER_FULL_NAME = os.getenv('SUPERUSER_FULL_NAME', 'changethis')
SUPERUSER_EMAIL = os.getenv('SUPERUSER_EMAIL', 'changethis@example.com')
SUPERUSER_PASSWORD = os.getenv('SUPERUSER_PASSWORD', 'changethis')
SUPERUSER_WEBHOOK = os.getenv('SUPERUSER_WEBHOOK', 'http://changethis.com')

# Application Specific
PROJECT_NAME = os.getenv('PROJECT_NAME')
TASK_TIMEOUT = 10  # 60 seconds

LOGGING_FORMAT = "<green>{time:YYYY-MM-DD at HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>"
LOGGING_CONFIG = {
    'handlers': [
        {'sink': sys.stdout, 'format': LOGGING_FORMAT, 'level': 'DEBUG'}
    ]
}

# Celery
CELERY_APP_NAME = 'Hydra'
