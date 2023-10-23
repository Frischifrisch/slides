import sys
import time

cnt = 0
num = 30
limit = 100000

class Count():
    def __init__(self):
        self.counter = 0
    def run(self):
        global cnt
        while self.counter < limit:
            self.counter += 1
            cnt += 1
        return

start = time.time()
for _ in range(num):
    c = Count()
    c.run()
end = time.time()

print(f"Expected: {num * limit}")
print(f"Received: {cnt}")
print(f"Elapsed: {end - start}")

# Expected: 3000000
# Received: 3000000
# Elapsed: 0.4130408763885498

