def Show_words():
    with open("notes.txt", "r") as file:
        for line in file:
            if len(line.split()) == 5:
                print(line, end="")


Show_words()
