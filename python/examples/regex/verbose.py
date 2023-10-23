import re

email = "foo@bar.com"

if m := re.search(r'\w[\w.-]*\@([\w-]+\.)+(com|net|org|uk|hu|il)', email):
    print('match')


if m := re.search(
    r'''
                \w[\w.-]*               # username
                \@
                ([\w-]+\.)+             # domain
                (com|net|org|uk|hu|il)  # gTLD
                ''',
    email,
    re.VERBOSE,
):
    print('match')
