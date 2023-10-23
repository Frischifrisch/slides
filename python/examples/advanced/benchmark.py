import timeit
from functools import reduce
import random

chars = [chr(65 + random.randrange(0, 26)) for _ in range(200)]
print(timeit.timeit('string = "".join(chars)',
    setup="from __main__ import chars", number=10000))

print(timeit.timeit('reduce(lambda x, y: x+y, chars)',
    setup="from __main__ import chars, reduce", number=10000))
