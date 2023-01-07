num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 >= num2:
    print(num1, " is largest.")
elif num2 >= num1: 
    print(num2, " is largest.")
else:
    print("Both are equal.")