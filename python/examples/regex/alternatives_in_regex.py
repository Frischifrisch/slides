import re

strings = [
    'apple pie',
    'banana pie',
    'apple'
]

for line in strings:
    if match := re.search(r'apple pie|banana pie', line):
        print('Matched in', line)
