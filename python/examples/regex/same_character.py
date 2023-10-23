import re

strings = [
    'banana',
    'apple',
    'infinite loop',
]

for line in strings:
    if match := re.search(r'(.)\1', line):
        print(match.group(0), 'matched in', line)
        print(match.group(1))
