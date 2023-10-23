import sys
filename = sys.argv[0]
with open(filename) as fh:
    lines = [line.rstrip("\n") for line in fh]
    print(lines)
