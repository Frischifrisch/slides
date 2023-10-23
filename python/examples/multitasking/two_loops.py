import multitasking
import time
import random

@multitasking.task
def first(count):
    sleep = random.randint(1,10)/2
    if count == 10:
        sleep = 10
    print(f"Start First {count} (sleeping for {sleep}s)")
    time.sleep(sleep)
    print(f"finish First {count} (after for {sleep}s)")

@multitasking.task
def second(count):
    sleep = random.randint(1,10)/2
    print(f"Start Second {count} (sleeping for {sleep}s)")
    time.sleep(sleep)
    print(f"finish Second {count} (after for {sleep}s)")

if __name__ == "__main__":
    for i in range(0, 10):
        first(i+1)
    multitasking.wait_for_tasks()
    print('first done')

    for i in range(0, 10):
        second(i+1)

    multitasking.wait_for_tasks()
    print('second done')
