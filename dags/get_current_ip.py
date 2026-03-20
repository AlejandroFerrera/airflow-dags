from datetime import datetime
from airflow.sdk import dag, task


@dag(
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["example"],
)
def get_current_ip():

    @task
    def get_ip():
        import socket
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Current IP Address: {ip_address}")
        return ip_address

    @task
    def print_ip_info(ip: str):
        print(f"IP Info: {ip}")

    ip = get_ip()
    print_ip_info(ip)


get_current_ip()
