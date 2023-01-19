num = int(input("Enter a number: "))
cop = num
res = 1
while num > 1:
    res *= num
    num -= 1
print("Factorial of", cop, "is", res)
