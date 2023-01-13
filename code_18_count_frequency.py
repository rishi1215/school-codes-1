d = {}
n = int(input("Enter number of elements: "))

for _ in range(n):
    a = input("Enter element: ")
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

print(d)


