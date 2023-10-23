import sys

if len(sys.argv) != 2:
    sys.stderr.write(f'Usage: {sys.argv[0]} FILENAME\n')
    exit()

file = sys.argv[1]
print(file)
with open(file) as f:
    for line in f:
        val = 30/int(line)

print('done')

