import os
import sys

exit_code = os.system("python process.py 5 2")
print(f'exit code: {exit_code // 256}')

