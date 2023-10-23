import sys
import module

# python finally.py one.txt zero.txt two.txt three.txt
files = sys.argv[1:]

for filename in files:
    try:
        module.read_and_divide(filename)
    except ZeroDivisionError as err:
        print(f"Exception {err} of type {type(err).__name__} in file {filename}")
    finally:
        print(f"In finally after trying file {filename}")
    print('')
