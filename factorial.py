num = int(input("Enter a number: "))
res = 1
while num > 1:
    res *= num
    num -= 1
print("Factorial of ", num, " is ", res)