import re

strings = [
    'abc',
    'text: #q#',
    'str: #a#',
    'text #b# more text',
    '#ab#',
    '#@#',
    '#.#',
    '# #',
    '##'
    '###'
]


for s in strings:
    print('str:  ', s)
    if match := re.search(r'#[abcdef@.]#', s):
        print('match:', match.group(0))
