import timeit
from functools import reduce

def add_in_loop(num):
    return sum(range(num+1))

def add_with_reduce(num):
    return reduce(lambda x, y: x + y, range(num+1))


def main():
    #num = 4
    #print(add_in_loop(num))
    #print(add_with_reduce(num))

    for num in [10, 1000]:
        print(f'num {num}')
        for name in ['add_in_loop', 'add_with_reduce']:
            print("{:16} {}".format(name, timeit.timeit(f'{name}({num})',
                number=100000,
                setup=f'from __main__ import {name}')))
        print()

if __name__ == "__main__":
    main()

