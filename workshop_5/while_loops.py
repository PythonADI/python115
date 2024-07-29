is_running: bool = True
queue_number: int = 1
while is_running: # infinite loop
    if queue_number == 30:
        is_running = False
    print(f"You are {queue_number} in queue: ")
    queue_number += 1


print("\nWith break statement:\n")
queue_number = 1
while True:
    answer: str = input("Press enter to grab a queue number or type 'exit' to stop: ")
    if answer.lower() == "exit":
        break
    print(f"You are {queue_number} in queue: ")
    queue_number += 1
