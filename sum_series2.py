
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
res = 0
for i in range(n + 1):
    num = i
    fact = 1
    while num > 1:
        fact *= num
        num -= 1
    res += (x**i) / fact
res = round(res,2)
print("Sum of the series is: ", res)
