# Fibbonaci Series

n = int(input("Enter number of terms: "))


def fibbonaci(n):

    x = 0
    y = 1

    if n < 1:
        return print("Number of terms should be positive")
    if n == 1:
        return print(x)
    print(x, y, end=" ")
    n -= 2
    while n > 0:
        print(x + y, end=" ")
        x, y = y, x + y
        n -= 1


fibbonaci(n)
