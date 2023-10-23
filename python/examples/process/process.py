import time
import sys

if len(sys.argv) != 3:
    exit(f"{sys.argv[0]} SECONDS EXIT_CODE")

seconds = int(sys.argv[1])
exit_code = int(sys.argv[2])

for sec in range(seconds):
    print(f"OUT {sec}", flush=True)
    print(f"ERR {sec}", file=sys.stderr)
    time.sleep(1)

exit(exit_code)
