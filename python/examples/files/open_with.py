filename = 'examples/files/numbers.txt'

with open(filename, 'r') as fh:
   print(fh)      # <open file 'numbers.txt', mode 'r' at 0x107084390>
   data = fh.read()
print(fh)      # <closed file 'numbers.txt', mode 'r' at 0x107084390>



with open(filename, 'r') as fh:
   print(fh)  # <open file 'numbers.txt', mode 'r' at 0x1070840c0>
   data = fh.read()
print(fh)     # <closed file 'numbers.txt', mode 'r' at 0x1070840c0>
