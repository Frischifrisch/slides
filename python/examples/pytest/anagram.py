from mymod_1 import is_anagram
import sys

if len(sys.argv) != 3:
    exit(f"Usage {sys.argv[0]} STR STR")

print(is_anagram(sys.argv[1], sys.argv[2]))

