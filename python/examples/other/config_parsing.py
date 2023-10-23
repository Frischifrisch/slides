import configparser
import sys

def parse():
  if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]}  FILEAME")
    exit()
  filename = sys.argv[1]

  cp = configparser.RawConfigParser()
  cp.read(filename)
  return cp

ini = parse()

for section in ini.sections():
  print(section)
  for v in ini.items(section):
    print(f"  {v[0]}  = {v[1]}")

