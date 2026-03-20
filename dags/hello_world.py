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

    # Log the current timestamp
    @task
    def log_timestamp():
        now = datetime.now().isoformat()
        print(f"Task completed at: {now}")

    # Pick a random emoji to display
    @task
    def random_emoji():
        import random
        emojis = ["🚀", "🎉", "🔥", "✨", "🐍", "☕", "🌈", "💡"]
        pick = random.choice(emojis)
        print(f"Today's emoji: {pick}")

    hello() >> random_number() >> log_timestamp() >> random_emoji()


hello_world()
