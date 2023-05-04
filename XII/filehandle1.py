with open("file2.txt") as file:    
    for line in file.readlines():
        print("#".join(line.split()))
    
    
