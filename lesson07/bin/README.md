# Apache Airflow Instructions

## Install Apache Airflow Locally

- Highly recommended to create new Python environment for Apache Airflow (e.g. with Anaconda or [Python venv](https://docs.python.org/3/library/venv.html)).

- Install Apache Airflow components with running `pip install -r requirements_dev.txt` in `lesson07\bin` folder.

- Set Airflow working folder with `export AIRFLOW_HOME=~/airflow` on Mac/Linux or `set AIRFLOW_HOME=%USERPROFILE%\airflow` on Windows.

- Start Apache Airflow locally with `airflow standalone`. Airflow creates `airflow.cfg` in the folder specified above with default settings.

- Go to `localhost:8080` in your browser to see Airflow administation app.