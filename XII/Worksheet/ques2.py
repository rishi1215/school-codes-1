def main():
    with open("poem.txt", "r") as f:
        content = f.read()
    count = content.lower().split().count("corona")
    print("Number of occurence of word corona:", count)
