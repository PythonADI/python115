''' docstring
customer service queue simulation
each customer needs 3 second to be served
50% chance of a customer arriving every second

display the queue number of each customer
- Who we are serving
- Who is in queue
'''
import time
import random

names: list[str] = [
    "Gio", "Nika", "Levani", "Marc", "Leon", "Mary", "Nina"
]

customers: list[tuple[int, str]] = []
queue_number: int = 1
last_update: float = time.time()
last_customer_arrive_time: float = time.time()
last_serve: float = time.time()

while True:
    more_than_one_sec = time.time() - last_update > 1
    we_served_the_customer = time.time() - last_serve > 3

    if more_than_one_sec:
        # customer spawning
        print(f"Customers in queue {customers}")
        chance = random.randint(0, 100)
        if chance >= 50:
            # print(time.time() - last_customer_arrive_time, chance)
            # print(f"Check if new customer has arrived number {queue_number}!")
            last_customer_arrive_time = time.time()
            customers.append(
                (queue_number, random.choice(names))
            )
            queue_number += 1

        last_update = time.time()

    if we_served_the_customer and len(customers) > 0:
        # customer serving
        customer_number, customer_name = customers.pop(0)
        print(f"Have a nice day {customer_name} [{customer_number}]")
        last_serve = time.time()
    

