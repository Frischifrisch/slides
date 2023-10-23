import re


line = "one 123 and two 123 and oxxo 23"

if match := re.search(r"(.)(.)\2\1", line):
    print(match.group(1)) # o
    print(match.group(2)) # x

if match := re.search(r"(\d\d).*\1", line):
    print(match.group(1)) # 12

if match := re.search(r"(\d\d).*\1.*\1", line):
    print(match.group(1)) # 23


if match := re.search(r"(\d\d).*\1{2,3}", "45 afjh 4545 kjdhfkh"):
    print(match.group(1)) # 45


# (.{5}).*\1

