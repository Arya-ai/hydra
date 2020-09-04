FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

LABEL maintainer="Aaditya Panikath <aaditya@arya.ai>"

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /tmp
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt