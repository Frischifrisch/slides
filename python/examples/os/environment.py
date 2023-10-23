import os

print(os.environ['HOME']) # /Users/gabor
print(os.environ.get('HOME')) # /Users/gabor

for k in os.environ:
    print("{:30} {}".format(k , os.environ[k]))
