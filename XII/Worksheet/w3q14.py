def TabDisplay():
    with open("topic.txt") as file:
        for line in file:
            for word in line.split():
                print("    ".join(word), end="    ")
            print()


TabDisplay()
