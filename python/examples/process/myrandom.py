import sys
import random
import time

def add_random(result_filename, count, wait, exception=''):
    total = sum(random.random() for _ in range(int(count)))
    time.sleep(float(wait))
    if exception:
        raise Exception(exception)

    with open(result_filename, 'w') as fh:
        fh.write(str(total))


if __name__ == '__main__':
    if len(sys.argv) not in [4, 5]:
        exit(f"Usage: {sys.argv[0]} RESULT_FILENAME COUNT WAIT [EXCEPTION]")
    add_random(*sys.argv[1:])
