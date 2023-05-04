def main():
    with open("poem.txt", "r") as f:
        content = f.read()
    count = content.lower().count("corona")
    print("Number of occurence of word corona:", count)
    
