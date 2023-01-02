# Input a list of numbers and swap elements at the even location with the elements at the odd location.
#  0 1 2 3 4 5 6
# [1,2,3,4,5,6,7]
# [2,1,4,3,6,5,7]

lis = input("Enter numbers separated by space: ").split()

for i in range(0, len(lis), 2):
    if len(lis) <= i+1:
        break
    lis[i], lis[i+1] = lis[i+1], lis[i] 
print(lis)
