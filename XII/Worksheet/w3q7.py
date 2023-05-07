def Show_capital():
    with open("notes.txt") as file:
        print(file.read().upper())


Show_capital()
