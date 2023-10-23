import random

def f():
    return sum(random.random() for _ in range(30))

def g():
    return random.random() * 30


def main(n):
    text = get_str(n)

    return sort(text)

def sort(s):
    chars = list(s)
    for i in reversed(range(len(chars))):
        a = f()
        b = g()
        for j in range(i, len(chars)-1):
            swap(chars, j)

    return ''.join(chars)

def get_str(n):
    return ''.join(chr(65 + random.randrange(0, 26)) for _ in range(1, n))

def swap(lst, loc):
    if lst[loc] > lst[loc + 1]:
        lst[loc], lst[loc + 1] = lst[loc + 1], lst[loc]

if __name__ == '__main__':
    print(main(1000))

