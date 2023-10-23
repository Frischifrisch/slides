import re

cases = [
    "hello!",
    "hello world.",
    "hello. world",
    ".",
]

for case in cases:
    print(case)
    if match := re.search(r'.', case):
        print(match.group(0))

print("----")

for case in cases:
    print(case)
    if match := re.search(r'\.', case):
        print(match.group(0))

print("----")

for case in cases:
    print(case)
    if match := re.search(r'[.]', case):
        print(match.group(0))

