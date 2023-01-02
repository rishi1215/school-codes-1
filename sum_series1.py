
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
res = 0
for i in range(n + 1):
    res += x**i

print("Sum of the series is: ", res)