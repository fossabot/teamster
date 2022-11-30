# Debian
ARG IMAGE_PYTHON_VERSION
FROM python:${IMAGE_PYTHON_VERSION}-slim

# update system pip
# trunk-ignore(hadolint/DL3013)
RUN python -m pip install --no-cache-dir --upgrade pip

# install system deps
# trunk-ignore(hadolint/DL3008)
RUN apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends \
        curl \
        gnupg \
        build-essential \
        msodbcsql18 \
        unixodbc-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# set the SHELL option -o pipefail before RUN with a pipe in
# https://github.com/codacy/codacy-hadolint/blob/a762bbf9decbe11c111e898fdee6dcb3f11a656b/codacy-hadolint/docs/description/DL4006.md
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# install Microsoft ODBC driver for SQL Server (Debian 11)
# https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16#debian18
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

# set env vars
ENV HOME="/root"

# FROM base

# copy project into container
# WORKDIR $HOME/app
# COPY ../requirements.txt ../pyproject.toml ./

# install project dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# FROM deps

WORKDIR $HOME/app
COPY ../requirements.txt ../pyproject.toml ./
COPY src/teamster ./src/teamster

# install project
RUN pip install --no-cache-dir .
