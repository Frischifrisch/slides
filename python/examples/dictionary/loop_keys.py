user = {
    'fname': 'Foo',
    'lname': 'Bar',
}

for key in user:
    print(key)

# lname
# fname

for key in user:
    print(f"{key} -> {user[key]}")

# lname -> Bar
# fname -> Foo
