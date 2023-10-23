import sys, csv

if len(sys.argv) != 2:
    sys.stderr.write(f"Usage: {sys.argv[0]} FILENAME\n")
    exit()

filename = sys.argv[1]
count = 0
with open(filename) as fh:
    for line in fh:
        line = line.rstrip("\n")
        row = line.split(';')
        #print(row)
        count += int(row[2])

print(f"Total: {count}")
