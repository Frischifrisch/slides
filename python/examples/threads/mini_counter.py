import threading
import sys

class ThreadedCount(threading.Thread):
    def run(self):
        for cnt in range(6):
            print(f"{cnt} {threading.current_thread().name}")
        return

a = ThreadedCount()
b = ThreadedCount()
c = ThreadedCount()

a.start()
b.start()
c.start()
print(f'main - Running {threading.active_count()} threads')

a.join()
b.join()
c.join()
print("main - thread is done")
