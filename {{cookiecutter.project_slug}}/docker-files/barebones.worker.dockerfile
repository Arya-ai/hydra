FROM python:3.7

LABEL maintainer="Aaditya Panikath <aaditya@arya.ai>"

ENV COLUMNS=80
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /tmp
COPY requirements-worker.txt .

RUN pip install --no-cache-dir -r requirements-worker.txt
