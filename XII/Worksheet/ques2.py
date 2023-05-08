def main():
    with open("poem.txt", "r") as f:
        content = f.read()
    count = content.split().count("Corona")
    print("Number of occurence of word corona:", count)
