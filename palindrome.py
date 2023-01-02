
orig_num = int(input("Enter a number: "))
num = orig_num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if rev == orig_num:
    print(orig_num, " is a Palindrome number.")