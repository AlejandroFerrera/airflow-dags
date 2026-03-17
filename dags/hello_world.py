from datetime import datetime
from airflow.sdk import dag, task


@dag(
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["example"],
)
def hello_world():

    @task
    def hello():
        print("Hello, World!")

    # Generate a random number after greeting
    @task
    def random_number():
        import random
        number = random.randint(1, 100)
        print(f"Your random number is: {number}")
        return number

    hello() >> random_number()


hello_world()
