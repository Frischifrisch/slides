import threading
import sys

class ThreadedCount(threading.Thread):
    def run(self):
        thread = threading.current_thread()
        print(f'{thread.name} - start')
        for c in range(10):
            print(f'{thread.name} - count {c}')
        print(f'{thread.name} - end')
        return

a = ThreadedCount()
b = ThreadedCount()
c = ThreadedCount()
a.start()
b.start()
c.start()

print(f'main - running {threading.active_count()} threads')

a.join()
b.join()
c.join()
print("main - thread is done")
