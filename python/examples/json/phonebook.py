import sys
import json
import os

def main():
    filename = 'phonebook.json'
    phonebook = {}
    if os.path.exists(filename):
        with open(filename) as fh:
            json_str = fh.read()
            phonebook = json.loads(json_str)

    if len(sys.argv) == 2:
        name = sys.argv[1]
        if name in phonebook:
            print(phonebook[name])
        else:
            print(f"{name} is not in the phonebook")
        return

    if len(sys.argv) == 3:
        name = sys.argv[1]
        phone = sys.argv[2]
        phonebook[name] = phone
        with open(filename, 'w') as fh:
            json_str = json.dumps(phonebook)
            fh.write(json_str)
        return

    print("Invalid number of parameters")
    print(f"Usage: {sys.argv[0]} username [phone]")

if __name__ == '__main__':
    main()
