import sys
import re

if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "FILE")
    exit()

filename = sys.argv[1]
with open(filename, 'r') as fh:
    for line in fh:
        print(line, end=" ")

        if match := re.search(r'REGEX1', line):
            print("   Matching 1", match.group(0))

        if match := re.search(r'REGEX2', line):
            print("   Matching 2", match.group(0))
