import sys
import module

# python else.py one.txt zero.txt two.txt three.txt
files = sys.argv[1:]

for filename in files:
    try:
        module.read_and_divide(filename)
    except ZeroDivisionError as err:
        print(f"Exception {err} of type {type(err).__name__} in file {filename}")
    else:
        print(f"In else part after trying file {filename} and succeeding")
            # Will run only if there was no exception.
    print()
