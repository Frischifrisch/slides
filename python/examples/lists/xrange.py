from __future__ import print_function
import sys

r = range(1000)
x = xrange(1000)

print(sys.getsizeof(r))  # 8072
print(sys.getsizeof(x))  # 40
