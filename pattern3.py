rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for _ in range(rows - i):
        print(end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
