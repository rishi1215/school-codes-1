def CountLower():
    with open("book.txt", "r") as f:
        text = f.read()
        print("Total lowercase characters:", len([a for a in text if a.islower()]))
