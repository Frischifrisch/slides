import threading
import random
import sys
import time

thread_count = 5

counter = 0
queue = list(map(lambda x: ('main', random.randrange(5)), range(20)))
#print(queue)

locker = threading.Lock()

class ThreadedCount(threading.Thread):
    def run(self):
        global counter
        my_counter = 0
        thread = threading.current_thread()
        print(f'{thread.name} - start thread')
        while True:
            locker.acquire()
            job = None
            if len(queue) > 0:
                counter += 1
                my_counter += 1
                job = queue[0]
                queue[:1] = []
            locker.release()
            if job is None:
                print(f'{thread.name} - no more jobs')
                break

            print(
                f'{thread.name} - working on job {counter} ({my_counter}) from {job[0]} sleep for {job[1]}'
            )
            time.sleep(job[1])

        return

threads = [ThreadedCount() for _ in range(thread_count)]
for t in threads:
    t.start()
for t in threads:
    t.join()
