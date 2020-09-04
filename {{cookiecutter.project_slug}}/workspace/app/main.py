import logging

from fastapi import FastAPI
from loguru import logger
from starlette.requests import Request
from starlette.responses import UJSONResponse

from app.api.v1.api import api_router
from app.core import config
from app.db.session import Session
from app.scripts.healthcheck import broker_healthcheck, db_healthcheck
from app.utils.loguru import InterceptHandler

logging.getLogger().handlers = [InterceptHandler()]


app = FastAPI(title=config.PROJECT_NAME, openapi_url=config.OPENAPI_URL)

app.include_router(api_router, prefix=config.API_V1_STR)


@app.on_event('startup')
async def setup_logger():
    logger.configure(**config.LOGGING_CONFIG)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get('/healthcheck', description="A health-check endpoint")
async def health_check():
    status = True
    response = dict()
    db_status, _ = db_healthcheck()
    broker_status, _ = broker_healthcheck()
    status = status and db_status and broker_status
    response["status"] = status
    if status:
        return UJSONResponse(response, status_code=200)
    else:
        response['errors'] = dict()
        # Add errors here
        return UJSONResponse(response, status_code=503)
