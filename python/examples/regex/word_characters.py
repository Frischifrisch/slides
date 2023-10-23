import re

values = [
    '2',
    '٣', # Arabic 3
    '½', # unicode 1/2
    '②', # unicode circled 2
    '߄', # NKO 4 (a writing system for the Manding languages of West Africa)
    '६', # Devanagari aka. Nagari (Indian)
    '_', # underscrore
    '-', # dash
    'a', # Latin a
    'á', # Hungarian
    'א', # Hebrew aleph

]

for val in values:
    print(val)
    if match := re.search(r'\w', val):
        print('Match ', match.group(0))

    if match := re.search(r'\w', val, re.ASCII):
        print('Match ASCII ', match.group(0))

