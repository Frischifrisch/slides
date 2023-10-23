import threading
import sys
import time
import random


results = []
locker = threading.Lock()

class ThreadedCount(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n = n

    def run(self):
        count = 0
        total = 0
        while count < 40000000 / self.n:
            rnd = random.random()
            total += rnd
            count += 1

        locker.acquire()
        results.append({'count': count, 'total': total})
        locker.release()
        return

def main():
    if len(sys.argv) != 2:
        exit("Usage: {} POOL_SIZE")
    size = int(sys.argv[1])
    start = time.time()
    threads = [ThreadedCount(n=size) for _ in range(size)]
    [ t.start() for t in threads ]
    [ t.join() for t in threads ]
    print(f"Results: {results}")
    totals = map(lambda r: r['total'], results)
    print(f"Total: {sum(totals)}")
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    main()
