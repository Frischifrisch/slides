import sys
import os

path_to_thing = sys.argv[1] if len(sys.argv) == 2 else __file__
print( os.path.basename(path_to_thing) )
print( os.path.dirname(path_to_thing) )
print( os.path.abspath(path_to_thing) )

print( os.path.exists(path_to_thing) )
print( os.path.isdir(path_to_thing) )
print( os.path.isfile(path_to_thing) )
