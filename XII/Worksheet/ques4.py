def dispS():
    with open("poem.txt", "r") as f:
        lines = f.readlines()
    
    for line in lines:
        if line.startswith("s") or line.startswith("S"):
            print(line.strip("\n"))

    
