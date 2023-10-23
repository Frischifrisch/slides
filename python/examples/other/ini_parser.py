import sys
import re

# Sample input data.ini

def parse():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} FILEAME")
    filename = sys.argv[1]
    data = {}
    # print("Dealing with " + filename)
    with open(filename) as fh:
        section = '__DEFAULT__'
        for line in fh:
            if re.match(r'^\s*(#.*)?$', line):
                continue
            if match := re.match(r'^\[([^\]]+)\]\s*$', line):
                # print('Section "{}"'.format(m.group(1)))
                section = match.group(1)
                continue
            if match := re.match(r'^\s*(.+?)\s*=\s*(.*?)\s*$', line):
                # print 'field :"{}"  value: "{}"'.format(m.group(1), m.group(2))
                if not data.get(section):
                    data[section] = {}
                data[section][ match.group(1) ] = match.group(2)

    return data

if __name__ == '__main__':
    ini = parse()
    print(ini)

