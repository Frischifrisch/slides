import re

strings = [
    'abc',
    'text: #q#',
    'str: #a#',
    'text #b# more text',
    '#a  and this? #c#',
    '#a  and this? # c#',
    '#@#',
    '#.#',
    '# #',
    '##'
    '###'
]

for s in strings:
    print('str:  ', s)
    if match := re.search(r'#.#', s):
        print('match:', match.group(0))
