FROM python:3.7.0-slim as base

LABEL maintainer="Aaditya Panikath <aaditya@arya.ai>"

ENV PYTHONBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.0.10 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

############### Barebones #################
FROM base as barebones

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

WORKDIR $PYSETUP_PATH


##################### API #####################
################ Base ################
FROM barebones as api-barebones

COPY ./requirements/api/poetry.lock ./requirements/api/pyproject.toml ./

RUN poetry install --no-dev

################ Dev ################
FROM base as api-development

WORKDIR $PYSETUP_PATH
COPY --from=api-barebones $POETRY_HOME $POETRY_HOME
COPY --from=api-barebones $PYSETUP_PATH $PYSETUP_PATH
RUN poetry install

WORKDIR /app/workspace
CMD ["./start.sh"]
###############################################



################### Worker #####################
################ Base ################
FROM barebones as worker-barebones

COPY ./requirements/worker/poetry.lock ./requirements/worker/pyproject.toml ./

RUN poetry install --no-dev

################ Dev ################
FROM base as worker-development

WORKDIR $PYSETUP_PATH
COPY --from=worker-barebones $POETRY_HOME $POETRY_HOME
COPY --from=worker-barebones $PYSETUP_PATH $PYSETUP_PATH
RUN poetry install

WORKDIR /app/workspace
CMD ["./start-worker.sh"]
###############################################



################ Stage ################
# No Stage at this point. Staging environments are used for testing

################ Production ################
# No Production at this point
# FROM base as production

# COPY --from=barebones $PYSETUP_PATH $PYSETUP_PATH
# COPY ../workspace /app/workspace

# WORKDIR /app/workspace
# RUN chmod +x start.sh
# CMD ["./start.sh"]
