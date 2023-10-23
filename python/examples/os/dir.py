import os
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} directory")

path = sys.argv[1]
files = os.listdir(path)

for name in files:
    print(name)
    print(os.path.join(path, name))
