FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

RUN apk --no-cache upgrade \
    && pip install --upgrade pip \
    && apk --no-cache add tzdata build-base gcc libc-dev g++ bash

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /api
WORKDIR /api

COPY ./app ./app
COPY ./alembic ./alembic
COPY ./alembic.ini ./alembic.ini
