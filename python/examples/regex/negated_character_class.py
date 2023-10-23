import re

text = "This is <a string> with some <sections> marks."

if m := re.search(r'<[^>]*>', text):
    print(m.group(0))
