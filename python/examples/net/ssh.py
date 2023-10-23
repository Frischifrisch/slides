import subprocess
import sys

if len(sys.argv) !=2:
    exit(f"Usage: {sys.argv[0]} hostname")

host = sys.argv[1]
command = "uname -a"

ssh = subprocess.Popen(["ssh", host, command],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if error := ssh.stderr.readlines():
    for err in error:
        sys.stderr.write(f"ERROR: {err}\n")
if result:
    print(result)
