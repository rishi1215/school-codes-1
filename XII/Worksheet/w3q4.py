def RevText() -> None:
    with open("input.txt", "r") as f:
        for line in f:
            line = [(a[::-1] if a.lower().startswith("i") else a) for a in line.split()]
            print(" ".join(line))


RevText()
