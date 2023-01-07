# Write a program to input n numbers from the user. Store these numbers in a tuple. Print the maximum, minimum, sum and mean of number from this tuple.

n = int(input("Enter number of elements: "))
tup = ()

for _ in range(n):
    haha = int(input("Enter number: "))
    tup = tup + (haha,)

print(
"\
Maximum number: {}\n\
Minimum number: {}\n\
Sum: {}\n\
Mean: {}\n\
".format(max(tup), min(tup), sum(tup), sum(tup)/len(tup))
)