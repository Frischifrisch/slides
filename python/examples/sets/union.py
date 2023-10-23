english = {'door', 'car', 'lunar', 'era'}
spanish = {'era', 'lunar', 'hola'}

all_the_words = english.union(spanish)

print(english)
print(spanish)
print(all_the_words)

# x = english + spanish # TypeError: unsupported operand type(s) for +: 'set' and 'set'
