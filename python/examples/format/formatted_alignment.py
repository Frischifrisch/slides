txt = "Some text"

print(f"'{txt}'")
print("'{:12}'".format(txt))  #  left:    'Some text   '
print("'{:<12}'".format(txt)) #  left:    'Some text   '
print("'{:>12}'".format(txt)) #  right:   '   Some text'
print("'{:^12}'".format(txt)) #  center:  ' Some text  '
