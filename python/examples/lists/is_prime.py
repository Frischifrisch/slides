import sys

n = int(sys.argv[1])

is_prime = all(n % i != 0 for i in range(2, int( n ** 0.5) + 1))
print(is_prime)


# math.sqrt(n) might be clearer than n ** 0.5

