import re

txt = 'text with slash \ and more text'
print(txt)         # text with slash \ and more text

if m1 := re.search('\\\\', txt):
    print('m1')    # m1

if m2 := re.search(r'\\', txt):
    print('m2')    # m2
