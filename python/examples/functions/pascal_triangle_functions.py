import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} N")

def get_next_row(row):
    if row == []:
        return [1]
    temp_row = [0] + row + [0]
    return [temp_row[ix]+temp_row[ix+1] for ix in range(len(temp_row)-1)]

def get_triangle(rows):
    triangle = []
    row = []
    for _ in range(0, rows):
        row = get_next_row(row)
        triangle.append(row)
    return triangle

def print_triangle(triangle):
    for row in triangle:
        print(row)

triangle = get_triangle(int(sys.argv[1]))
print_triangle(triangle)
