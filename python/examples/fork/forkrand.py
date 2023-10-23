import os, time, random

print(f'{os.getpid()} - start running')

pid = os.fork()
if not pid:
    #random.seed()
    print(f'{os.getpid()} - in child')
    print(random.random())
    time.sleep(1)
    exit(3)

print(f'{os.getpid()} - in parent (child pid is {pid})')
print(random.random())

done = os.wait()
print(f'{os.getpid()} - Child exited {done}')

