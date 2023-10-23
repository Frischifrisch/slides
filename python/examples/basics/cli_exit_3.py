import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} VALUE")
        exit(3)
    print(f"Hello {sys.argv[1]}")

main()
