def main():
    try:
        with open('colors.txt') as fh:
            colors = [line.rstrip("\n") for line in fh]
    except IOError:
        print("Could not open colors.txt")
        exit()

    for i in range(len(colors)):
        print(f"{i}) {colors[i]}")

    c = int(input("Select color: "))
    print(colors[c])

main()
