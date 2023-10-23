import threading
import sys

num_threads, count_till = 3, 5

class ThreadedCount(threading.Thread):
    def run(self):
        thread = threading.current_thread()
        print(f'{thread.name} - start')
        for cnt in range(count_till):
            print(f'{thread.name} - count {cnt}')
        print(f'{thread.name} - end')
        return

threads = [ThreadedCount() for _ in range(num_threads)]
for th in threads:
    th.start()

print(f'main - running {threading.active_count()} threads')

for th in threads:
    th.join()
print("main - thread is done")
