import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} N")

rows = int(sys.argv[1])

row = []
for _ in range(0, rows):
    if row == []:
        next_row = [1]
    else:
        temp_row = [0] + row + [0]
        next_row = [temp_row[ix]+temp_row[ix+1] for ix in range(len(temp_row)-1)]
    row = next_row
    print(row)

