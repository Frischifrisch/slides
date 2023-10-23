age = float(input('Please type in your age: '))
if age >= 21:
    print('You can already drink alcohol. In the USA as well.')
elif age >= 18:
    print('You can already drink alcohol. (But not in the USA.)')
else:
    print('You cannot legally drink alcohol.')
