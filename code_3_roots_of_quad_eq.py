# Find roots of quadratic equation
a = int(input("Enter value of coefficient of x²: "))
b = int(input("Enter value of coefficient of x: "))
c = int(input("Enter value of the constant term: "))

d = b**2 - 4 * a * c
if d < 0:
    print("Roots of the equation are imaginary.")
else:
    roots = [(-b + d**0.5) / (2 * a), (-b - d**0.5) / (2 * a)]
    if d == 0:
        print("Root of the equation is {:.2f}".format(roots[0]))
    else:
        print("Roots of the equation are {:.2f} and {:.2f}".format(*roots))
