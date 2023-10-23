import re

text = 'The black cat climed'
if match := re.search(r'lac', text):
    print("Matching")       # Matching
    print(match.group(0))   # lac

if match := re.search(r'dog', text):
    print("Matching")
else:
    print("Did NOT match")
    print(match)     # None
