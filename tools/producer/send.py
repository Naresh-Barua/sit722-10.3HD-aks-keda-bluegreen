import os
import sys
from azure.servicebus import ServiceBusClient, ServiceBusMessage

def send_messages(connection_str, queue_name, count=10):
    with ServiceBusClient.from_connection_string(conn_str=connection_str) as client:
        sender = client.get_queue_sender(queue_name=queue_name)
        with sender:
            for i in range(count):
                msg = ServiceBusMessage(f"order-{i}")
                sender.send_messages(msg)
                print(f"Sent: order-{i}")

if __name__ == "__main__":
    conn = os.getenv("SERVICEBUS_CONNECTION")
    queue = os.getenv("SERVICEBUS_QUEUE", "orders-queue")
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 10

    if not conn:
        print("Error: SERVICEBUS_CONNECTION env var not set")
        sys.exit(1)

    send_messages(conn, queue, count)

