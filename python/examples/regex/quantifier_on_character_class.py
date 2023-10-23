import re

strings = (
    "-a-",
    "-b-",
    "-x-",
    "-aa-",
    "-ab-",
    "--",
)

for line in strings:
    if match := re.search(r'-[abc]-', line):
        print(line)
print('=========================')

for line in strings:
    if match := re.search(r'-[abc]+-', line):
        print(line)
print('=========================')

for line in strings:
    if match := re.search(r'-[abc]*-', line):
        print(line)


