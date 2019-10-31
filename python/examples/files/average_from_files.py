import sys


def main():
    for filename in sys.argv[1:]:
        try:
            #do_some_stuff(filename)
            with open(filename) as fh:
                total = 0
                count = 0
                for line in fh:
                    number = float(line)
                    total += number
                    count += 1
                print("Average: ", total/count)
        except Exception:
            print("trouble with {}".format(filename))

main()
