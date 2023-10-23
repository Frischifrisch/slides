def read_and_divide(filename):
    print(f"before {filename}")
    with open(filename, 'r') as fh:
        number = int(fh.readline())
        print(100 / number)
    print(f"after  {filename}")
