import subprocess
import sys

ssh = subprocess.Popen([r"c:\Users\foobar\download\plink.exe", "-ssh",
                    "foobar@username-or-ip",
                    "-pw", "password",
                    "-C", "uname -a"],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if error := ssh.stderr.readlines():
    for err in error:
        sys.stderr.write(f"ERROR: {err}\n")
if result:
    print(result)
