with open("file.txt") as file:
    for line in file.readlines():
        print("#".join(line.split()))
    print()
    