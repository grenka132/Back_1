FROM python:3.12-alpine

WORKDIR /app

ENV PYTHONPATH .
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk add --no-cache uv \
    && apk add --no-cache curl \
    && apk add --no-cache make

COPY pyproject.toml ./

COPY ./src ./src
COPY ./alembic.ini ./alembic.ini
COPY ./migrations ./migrations
COPY ./Makefile ./Makefile

EXPOSE 8000

CMD make run_for_docker
