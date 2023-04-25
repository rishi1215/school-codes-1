with open("file.txt") as file:
    for i in range(5):
        print(file.readline(), end = "")