#!/bin/bash

# update apt packages
sudo apt-get -qq -y update --no-install-recommends &&
	sudo apt-get -qq -y upgrade --no-install-recommends &&
	sudo apt-get -qq autoremove -y &&
	sudo apt-get -qq clean -y

# update pip
python -m pip install --no-cache-dir --upgrade pip

# update pdm
sudo pdm self update

# update trunk
trunk upgrade -y --no-progress

# set up dbt env
mkdir -p ~/.dbt
sudo mkdir -p /etc/secret-volume
sudo echo "${DBT_USER_CREDS}" >/etc/secret-volume/dbt_user_creds_json
