import re

strings = [
    'apple pie',
    'banana pie',
    'apple'
]

for line in strings:
    match = re.search(r'apple pie|banana pie', line)
    if match:
        print('Matched in', line)
