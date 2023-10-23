import sys

def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} VALUE")
    print(f"Hello {sys.argv[1]}")

main()
