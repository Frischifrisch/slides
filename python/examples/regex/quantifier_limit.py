import re

strings = (
    "axxxa",
    "axxxxa",
    "axxxxxa",
)

for text in strings:
    if match := re.search(r'ax{4}', text):
        print(f"Match {text}")
        print(match.group(0))
    else:
        print("NOT Match")
