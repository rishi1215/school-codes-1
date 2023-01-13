num = int(input("Enter a number: "))
num_copy = num
check = num
order = 0  # no. of digits
while num > 0:
    order += 1
    num = num // 10
res = 0
while num_copy > 0:
    rem = num_copy % 10
    res += rem**order
    num_copy = num_copy // 10
if res == check:
    print(check, " is an Armstrong number")
else:
    print(check, " is not an Armstrong number")
