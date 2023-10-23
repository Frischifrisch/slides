import sys
import module

# python handle_both_exceptions.py one.txt zero.txt two.txt three.txt
files = sys.argv[1:]

for filename in files:
    try:
        module.read_and_divide(filename)
    except ZeroDivisionError:
        print(f"Cannot divide by 0 in file {filename}")
    except IOError:
        print(f"Cannot open file {filename}")
    except Exception as ex:
        print(f"Exception type {type(ex).__name__} {ex} in file {filename}")


