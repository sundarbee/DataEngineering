from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator

default_args = {
    "Owner": "airflow",
    "retries": 0,
    "start_date": datetime(2020,4,4)
}
dag = DAG(dag_id="First_DAG_for_test", default_args=default_args,
          catchup=False, schedule_interval='@hourly')

download_images = BashOperator(
    task_id='print_data',
    bash_command='python3 /Users/sundarb/Desktop/print.py',
    dag=dag,
)

config_csv = BashOperator(
    task_id = 'read_csv',
    bash_command = 'python3 /Users/sundarb/Documents/DEWorkspace/postgresSample.conf',
    dag = dag
)

start = DummyOperator(task_id='start_check',dag=dag)
end = DummyOperator(task_id='end',dag=dag)


start >> end >> download_images >> config_csv