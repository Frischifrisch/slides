import random

def calc(num):
    random.seed(num)
    return sum(random.random() for _ in range(10000000))
