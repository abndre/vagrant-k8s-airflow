import time
from pprint import pprint
import pendulum

from airflow import DAG
from airflow.decorators import task

with DAG(
    dag_id='segunda_dag',
    schedule="5 * * * *",
    start_date=pendulum.datetime(2022, 5, 11, 15,45, tz="America/Sao_Paulo"),
    catchup=False,
    tags=['example'],
) as dag:

    # [START howto_operator_python]
    @task(task_id="print_the_context")
    def print_context(ds=None, **kwargs):
        """Print the Airflow context and ds variable from the context."""
        #pprint(kwargs)
        print(ds)
        return 'Whatever you return gets printed in the logs'

    run_this = print_context()

run_this