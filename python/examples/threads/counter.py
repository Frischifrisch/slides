import threading
import sys

class ThreadedCount(threading.Thread):
    def __init__(self, name, start, stop):
        super().__init__()
        self.name = name
        self.counter = start
        self.limit = stop
        print(f'__init__  of {self.name} in {threading.current_thread()}')

    def run(self):
        print(f'start run of {self.name} in {threading.current_thread()}')
        while self.counter < self.limit:
            print(f'count {self.name} of {self.counter}')
            self.counter += 1
        print(f'end run   of {self.name} in {threading.current_thread()}')
        return

foo = ThreadedCount("Foo", 1, 11)
bar = ThreadedCount("Bar", 1, 11)
foo.start()
bar.start()
print(f'main - running {threading.active_count()} threads')
foo.join()
bar.join()
print("main - thread is done")
