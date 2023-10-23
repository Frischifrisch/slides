def cycle(values=[]):
    my_values = []
    for v in values:
        my_values.append(v)
        yield v
    while True:
        yield from my_values

i = 0
for c in cycle(['A', 'B', 'C']):
    print(c)
    i += 1
    if i >= 4:
        break
