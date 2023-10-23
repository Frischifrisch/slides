import sys

def hello(name):
    msg = f'{name}!!!!'
    print(f'Hello {msg}')

def main():
    hello(sys.argv[1])

main()
