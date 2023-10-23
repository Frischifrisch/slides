import re

line = 'Start   blabla End'

text = '''
prefix
Start
blabla
End
postfix
'''

regex = r'^Start[\d\D]*End$'
if m := re.search(regex, line):
    print('line')

if m := re.search(regex, text):
    print('text')

print('-' * 10)

if m := re.search(regex, line, re.MULTILINE):
    print('line')

if m := re.search(regex, text, re.MULTILINE):
    print('text')
