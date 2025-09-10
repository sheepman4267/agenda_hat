FROM python:3.11-alpine

RUN apk add bash

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ARG HAT_DEBUG='False'
ARG HAT_STATIC_ROOT='/static-root'
ARG HAT_ALLOWED_HOSTS='0.0.0.0'
ARG HAT_SQLITE3_PATH='/db/db.sqlite3'


ENV HAT_DEBUG=${HAT_DEBUG}
ENV HAT_SECRET_KEY=${HAT_SECRET_KEY}
ENV HAT_STATIC_ROOT=${HAT_STATIC_ROOT}
ENV HAT_ALLOWED_HOSTS=${HAT_ALLOWED_HOSTS}
ENV HAT_SQLITE3_PATH=${HAT_SQLITE3_PATH}

EXPOSE 8000/

ENTRYPOINT echo Migrating.. \
    && python manage.py migrate \
    && python manage.py collectstatic --no-input \
    && honcho start