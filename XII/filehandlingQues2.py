def AM_Count():
    with open("poem.txt") as file:
        poem = file.read()
        a = poem.count("a") + poem.count("A")
        m = poem.count("m") + poem.count("M")
        print("Occurence of A: {}\nOccurence of M: {}".format(a,m))