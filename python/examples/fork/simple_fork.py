import os
import time

print(f'{os.getpid()} - start running')

pid = os.fork()
if not pid:
    print(f'{os.getpid()} - in child. Parent is {os.getppid()}')
    time.sleep(1)
    exit(3)

print(f'{os.getpid()} - in parent (child pid is {pid})')

child_pid, exit_code = os.wait()
print(
    f'{os.getpid()} - Child with pid {child_pid} exited. Exit code {exit_code}'
)
print(f'Real exit code {int(exit_code / 256)}')
print(f'Also known as {exit_code >> 8}')
