import sys
import datetime
import random

def main():
    limit = get_limit()
    print(limit)

    date = datetime.datetime.now()

    rnd = random.randrange(2, 6)
    print(rnd)

    count(limit)
    print("after count")

def get_limit():
    return int(sys.argv[1]) if len(sys.argv) == 2 else 10

def count(limit):
    for ix in range(limit):
        div = ix - 12
        show(ix, ix / div)

def show(number, result):
    print(number, result)


if __name__ == '__main__':
    main()
