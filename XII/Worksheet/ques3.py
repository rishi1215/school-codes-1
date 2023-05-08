def main() -> None:
    with open("poem.txt", "r") as f:
        lines: list[str] = f.readlines()
    for line in lines:
        for word in line.split():
            word = word.strip("\n")
            if len(word) == 2:
                print(word, end = " ")

    
main()