import sys
import csv

if len(sys.argv) != 2:
    sys.stderr.write(f"Usage: {sys.argv[0]} FILENAME\n")
    exit()

filename = sys.argv[1]
count = 0
with open(filename) as fh:
    rd = csv.reader(fh,
        delimiter=';',
        #strict=True,
    )

    for row in rd:
        print(row)
        count += int(row[2])

print(f"Total: {count}")

