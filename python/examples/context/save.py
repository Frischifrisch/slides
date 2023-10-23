import os

for ix in range(10):
    filename = f'data{ix}.txt'
    with open(filename, 'w') as fh:
        fh.write('hello')
        if ix == 0:
            break
stat = os.stat(filename)
print(stat.st_size)    # 0,   the file has not been saved yet
