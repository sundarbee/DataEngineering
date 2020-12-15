import psycopg2
import kafka
from json import dumps
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from datetime import datetime

with DAG(
    "Airflow_task",
    description="Dag is to write data to Elasticsearch",
    schedule_interval="*/5 * * * *",
    start_date=datetime(2018, 7, 9),
    catchup=False,
) as dag:

    def task_1():
        try:
            connection = psycopg2.connect(
                user="sundarb",
                password="P7BrSBgxVfuYz4ZB",
                host="localhost",
                port="5432",
                database="test_aut",
            )
            cursor = connection.cursor()

            postgresSQL_select_Query = "select * from test_de"

            cursor.execute(postgresSQL_select_Query)
            user_record = cursor.fetchall()
            # print(user_record)
            producer = kafka.KafkaProducer(
                bootstrap_servers=["localhost:9092"],
                value_serializer=lambda x: dumps(x).encode("utf-8"),
            )

            for record in user_record:
                id_, name1, name2, name3 = record
                print(name1)
                data = {"name": name1}
                producer.send("trump", value=data)

        except (Exception, psycopg2.Error) as error:
            print("Error:::::", str(error))
        else:
            if connection:
                cursor.close()
                connection.close()
                print("connection closed")

    task1 = PythonOperator(task_id="Data_from_table1", python_callable=task_1)

    def task_2():
        try:
            connection = psycopg2.connect(
                user="sundarb",
                password="P7BrSBgxVfuYz4ZB",
                host="localhost",
                port="5432",
                database="test_aut",
            )
            cursor = connection.cursor()

            postgresSQL_select_Query = "select * from table_1"

            cursor.execute(postgresSQL_select_Query)
            user_record = cursor.fetchall()
            # print(user_record)
            producer = kafka.KafkaProducer(
                bootstrap_servers=["localhost:9092"],
                value_serializer=lambda x: dumps(x).encode("utf-8"),
            )

            for record in user_record:
                id_, name1, name2, name3, name4, name5 = record
                print(name1)
                data = {"name": name1}
                producer.send("trump", value=data)

        except (Exception, psycopg2.Error) as error:
            print("Error:::::", str(error))
        else:
            if connection:
                cursor.close()
                connection.close()
                print("connection closed")
task2 = PythonOperator(task_id="Data_from_table2", python_callable=task_2)

task1 >> task2