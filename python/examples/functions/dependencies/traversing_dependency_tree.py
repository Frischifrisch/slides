import sys
import os

if len(sys.argv) < 2:
   exit(f"Usage: {sys.argv[0]} NAME")

start = sys.argv[1]

def get_dependencies(name):
   print(f"Processing {name}")

   deps = set(name)
   filename = f"{name}.txt"
   if not os.path.exists(filename):
       return deps

   with open(filename) as fh:
       for line in fh:
           row = line.rstrip("\n")
           deps.add(row)
           deps.update( get_dependencies(row) )

   return deps

dependencies = get_dependencies(start)
print(dependencies)

