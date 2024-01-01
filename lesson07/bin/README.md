# Apache Airflow Instructions

=======
## Install Apache Airflow Locally using reference container image


1) First you need to install docker on your windows. Run command from command prompt if you get sure that docker installed successfully
    ```
    docker version
    ```
2) Then you need to pull airflow image using command 
    ```
    docker pull puckel/docker-airflow
    ``` 
3) Next step is to run image 
    ```
    docker run -d -p 8080:8080 puckel/docker-airflow webserver
    ```
    This will run airflow and you can access webUI at localhost:8080. Go to `localhost:8080` in your browser to see Airflow administation app.

To copy dags use command 
    ```
    docker cp sample_dag.py containerName:/usr/local/airflow/dags
    ```
To access airflow utility you need to access the bash shell of container
    ```
    docker exec -it containerName bash
    ``` 
Once you inside bash shell you can run command line utilities ex **airflow list_dags**


=======
## Install Apache Airflow Locally

- Highly recommended to create new Python environment for Apache Airflow (e.g. with Anaconda or [Python venv](https://docs.python.org/3/library/venv.html)).

- Install Apache Airflow components with running `pip install -r requirements_dev.txt` in `lesson07\bin` folder.

- Set Airflow working folder with `export AIRFLOW_HOME=~/airflow` on Mac/Linux or `set AIRFLOW_HOME=%USERPROFILE%\airflow` on Windows.

- Start Apache Airflow locally with `airflow standalone`. Airflow creates `airflow.cfg` in the folder specified above with default settings.

- Go to `localhost:8080` in your browser to see Airflow administation app.

