# https://hub.docker.com/_/python
ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-slim

# set container envs
ARG CODE_LOCATION
ENV DBT_PROFILES_DIR /app/src/dbt/${CODE_LOCATION}
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set workdir
WORKDIR /app

# install dependencies
COPY pyproject.toml ./pyproject.toml
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install . --no-cache-dir --verbose

# install python project
COPY src/teamster/ ./src/teamster/
RUN pip install . --no-cache-dir

# install dbt project
COPY src/dbt/ ./src/dbt/
RUN dbt clean --project-dir ${DBT_PROFILES_DIR} \
    && dbt deps --project-dir ${DBT_PROFILES_DIR} \
    && dbt parse --project-dir ${DBT_PROFILES_DIR}