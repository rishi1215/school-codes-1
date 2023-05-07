def countlines():
    with open("story.txt") as file:
        lines = file.readlines()

    count = 0
    for line in lines:
        if line[0] in "aA":
            count += 1
    print("Number of lines starting with 'a' or 'A':", count)


countlines()
