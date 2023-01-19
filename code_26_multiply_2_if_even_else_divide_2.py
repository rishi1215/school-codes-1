n = int(input("Enter number of elements: "))
l = []
for i in range(n):
    l.append(int(input("Enter element: ")))
while n > 0:
    if l[n - 1] % 2 == 0:
        l[n - 1] *= 2
    else:
        l[n - 1] /= 2
    n -= 1
print(l)
