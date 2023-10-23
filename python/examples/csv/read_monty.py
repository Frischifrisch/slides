import sys
import csv

if len(sys.argv) != 2:
    sys.stderr.write(f"Usage: {sys.argv[0]} FILENAME\n")
    exit()

filename = sys.argv[1]

with open(filename) as fh:
    rd = csv.DictReader(fh, delimiter=',')
    for row in rd:
        print(row)
