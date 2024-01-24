#!/usr/bin/env bash
# NB:install Apache Airflow first using install_airflow.sh script

# TODO: Change this to the path where airflow directory is located
# (default is ~/airflow)
export AIRFLOW_HOME=/home/user/repos/DataEngineering.d/Data-Engineering-Golovata/lesson07/airflow
# fixes issue on Mac:
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
export no_proxy="*"
# fixes issue with Pendulum library running in Ubuntu:
export TZ=Europe/Kiev

airflow standalone
