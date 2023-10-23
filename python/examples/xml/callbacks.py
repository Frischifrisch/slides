import xml.parsers.expat
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

file = sys.argv[1]


def start_element(name, attrs):
    print(f'Start element: {name} {attrs}')


def end_element(name):
    print(f'End element: {name}')


def char_data(data):
    print(f'Character data: {repr(data)}')


p = xml.parsers.expat.ParserCreate()

p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data

p.ParseFile(open(file, 'rb'))

print('done')
