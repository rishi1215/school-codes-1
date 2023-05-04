def main():
    with open("poem.txt", "r") as f:
        lines = file.readlines()
    for line in lines:
        for word in line.split():
            word = word.split("\n")
            if len(word) == 2:
                print(word, end = " ")

    
