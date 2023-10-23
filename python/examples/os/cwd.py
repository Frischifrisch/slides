import sys
import os

to_dir = sys.argv[1] if len(sys.argv) == 2 else '..'
current_dir = os.getcwd()
print(current_dir)

os.chdir(to_dir)

new_dir = os.getcwd()
print(new_dir)
