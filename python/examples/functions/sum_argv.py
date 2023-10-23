import sys

def mysum(*numbers):
    print(numbers)
    return sum(numbers)

v = [int(x) for x in sys.argv[1:] ]
r = mysum( *v )
print(r)
