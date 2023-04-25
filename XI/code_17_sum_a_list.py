# print("Sum of all numbers is ", sum(map(int, input("Enter numbers: ").split())))


print("Write `DONE` when done inputting all numbers")
l = []
while True:
    _ = input("")
    if _ == "DONE":
        break
    l.append(int(_))
print("Sum of numbers is {}".format(sum(l)))
