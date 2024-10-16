ARG PYTHON_VERSION=3.12.7-alpine3.20

FROM python:${PYTHON_VERSION}

ARG POETRY_VERSION="1.8.3"
ENV POETRY_HOME="/opt/poetry"
ENV PATH="${POETRY_HOME}/bin:${PATH}"
