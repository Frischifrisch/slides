import timeit

def one_by_one():
    import random
    return "".join(chr(65 + random.randrange(0, 26)) for _ in range(200))

def at_once():
    import random
    chars = [chr(65 + random.randrange(0, 26)) for _ in range(200)]
    return ''.join(chars)

print(timeit.timeit('one_by_one()',
    setup="from __main__ import one_by_one", number=10000))

print(timeit.timeit('at_once()',
    setup="from __main__ import at_once", number=10000))

