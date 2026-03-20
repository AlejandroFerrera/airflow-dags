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

    # Print a random motivational quote
    @task
    def random_quote():
        import random
        quotes = [
            "The best time to plant a tree was 20 years ago. The second best time is now.",
            "Done is better than perfect.",
            "Keep it simple, stupid.",
            "First, solve the problem. Then, write the code.",
            "Talk is cheap. Show me the code.",
        ]
        print(f"Quote of the day: {random.choice(quotes)}")

    # Get system hostname
    @task
    def get_hostname():
        import socket
        hostname = socket.gethostname()
        print(f"System Hostname: {hostname}")
        return hostname

    hello() >> random_number() >> log_timestamp() >> random_emoji() >> random_quote() >> get_hostname()


hello_world()
