# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
# from airflow.operators.bash_operator import BashOperator
# from datetime import datetime
# import psycopg2
# from psycopg2 import sql

# with DAG(
#     "Controlling_a_DAG_with_the_terminal",
#     description="This DAG is to practice terminal commands to control airflow.",
#     schedule_interval="*/5 * * * *",
#     start_date=datetime(2018, 11, 1),
#     catchup=False,
# ) as dag:
    # def create_schema(ds, **kwargs):
    #     print("Remotely received value of {} for key = message".format(
    #         kwargs['dag_run'].conf['client_name']))
    #     try:
    #         conn = psycopg2.connect(database="sundarb", host="localhost")
    #         cursor = conn.cursor()
    #         schema_name = kwargs['dag_run'].conf['client_name']
    #         cursor.execute(
    #             sql.SQL("create schema {}")
    #             .format(sql.Identifier(schema_name)))
    #         conn.commit()
    #         print('test')
    #     except(Exception, psycopg2.DatabaseError) as error:
    #         print(error)
#     test_task = PythonOperator(
#         task_id="test_task",
#         python_callable=create_schema,
#         provide_context=True
#     )

#     # bash_task = BashOperator(
#     # task_id = "bash-task",
#     # bash_command='echo "Here is the message: '
#     # '{{ dag_run.conf["message"] if dag_run else "" }}" ',
#     # )
#     test_task

from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow import DAG
import psycopg2
from psycopg2 import sql


args = {
    'start_date': '2018,11,1',
    'owner': 'airflow',
}

dag = DAG(
    dag_id='example_dag_conf',
    default_args=args,
    schedule_interval=None,
)


def run_this_func(ds, **kwargs):
    print("Remotely received value of {} for key=message".
          format(kwargs['dag_run'].conf['client_1']))
    try:
        conn = psycopg2.connect(database="sundarb", host="localhost",port="5433")
        cursor = conn.cursor()
        schema_name = kwargs['dag_run'].conf['client_1']
        cursor.execute(
            sql.SQL("create schema {}")
            .format(sql.Identifier(schema_name)))
        conn.commit()
        print('test')
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


run_this = PythonOperator(
    task_id='run_this',
    provide_context=True,
    python_callable=run_this_func,
    dag=dag,
)

# You can also access the DagRun object in templates
bash_task = BashOperator(
    task_id="bash_task",
    bash_command='echo "Here is the message: '
                 '{{ dag_run.conf["client_1"] if dag_run else "" }}" ',
    dag=dag,
)
