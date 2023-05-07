def HashDisplay():
    with open("matter.txt") as file:
        content = file.read()

    for chr in content:
        print(chr, end="#")


HashDisplay()
