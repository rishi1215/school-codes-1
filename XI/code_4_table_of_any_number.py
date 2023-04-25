# Print table of any number

num = int(input("Enter a number: "))

for n in range(1, 11):
    print("{} X {} = {}".format(num, n, num * n))
