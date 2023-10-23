more = ['Joe Doe', 'Jane Doe']
names = ['Foo Bar', 'Orgo Morgo', *more]
print(names)  # ['Foo Bar', 'Orgo Morgo', 'Joe Doe', 'Jane Doe']

names = ['Foo Bar', 'Orgo Morgo', more]
print(names) # ['Foo Bar', 'Orgo Morgo', ['Joe Doe', 'Jane Doe']]

names = ['Foo', 'Bar', 'Qux']
print(names)   # ['Foo', 'Bar', 'Qux']

names = ['Foo', 'Bar']
names.extend('Qux')
print(names)   # ['Foo', 'Bar', 'Q', 'u', 'x']
