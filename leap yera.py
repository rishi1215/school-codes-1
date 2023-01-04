# Condition for a leap year
# 1. Should be divisible by 4 and not 100 (XXXX)
# 2. Should be divisible by 400 (XX00)
year = int(input("Enter year: "))
if (year%4==0 and year%100 != 0) or (year%400):
    print(year, " is a leap year.")
else:
    print(year, " is not a leap year.")
