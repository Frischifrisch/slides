import sys
import time
from mymodule import calc

def main(n):
    print(f"do 1-{n}")
    return {ix: calc(ix) for ix in range(1, n)}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} NUMBER")

    start = time.time()
    results = main(1+int(sys.argv[1]))
    end = time.time()
    total = sum(results.values())
    print(f"Total: {total}")
    print(f"Elapsed time: {end - start}")



