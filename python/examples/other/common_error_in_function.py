import sys

def check():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} Number")

    if int(sys.argv[1]) > 42:
        res = "bigger"
    elif int(sys.argv[1]) < 42:
        res = "smaller"

    print(res)

check()

# UnboundLocalError: local variable 'res' referenced before assignment
