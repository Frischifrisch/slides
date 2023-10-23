import re

line = 'Before <div>content</div> After'

text = '''
Before
<div>
content
</div>
After
'''

if match := re.search(r'<div>.*</div>', line):
    print(f"line '{match.group(0)}'");

if match := re.search(r'<div>.*</div>', text):
    print(f"text '{match.group(0)}'");

print('-' * 10)

if match := re.search(r'<div>.*</div>', line, re.DOTALL):
    print(f"line '{match.group(0)}'");

if match := re.search(r'<div>.*</div>', text, re.DOTALL):
    print(f"text '{match.group(0)}'");

