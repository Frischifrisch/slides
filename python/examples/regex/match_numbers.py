import re

line = 'There is a phone number 12345 in this row and an age: 23'

if match := re.search(r'\d+', line):
    print(match.group(0))  # 12345
