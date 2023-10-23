import re

def parse_file(filename):
    data = {}
    with open(filename) as fh:
        for row in fh:
            row = row.rstrip("\n")
            if re.search(r'=', row):
                k, v = re.split(r'\s*=\s*', row)
                data[k] = v
    return data

def save_file(filename, data):
    with open(filename, 'w') as fh:
        for k in data:
            fh.write(f"{k}={data[k]}\n")

if __name__ == '__main__':
    print(parse_file('a.cfg'))
