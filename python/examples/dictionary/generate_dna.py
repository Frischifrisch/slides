import sys
import random

if len(sys.argv) != 2:
    exit("Need a number")
count = int(sys.argv[1])

dna = [random.choice(['A', 'C', 'T', 'G']) for _ in range(count)]
print(''.join(dna))

