import sys
import editdistance

def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} filename")
    filename = sys.argv[1]
    outfile = 'out.txt'

    rows = []
    with open(filename) as fh:
        rows.extend(row.rstrip("\n") for row in fh)
    with open(outfile, 'w') as fh:
        for a in rows:
            for b in rows:
                dist = editdistance.eval(a, b)
                fh.write(f"{a},{b},{dist}\n")

main()
