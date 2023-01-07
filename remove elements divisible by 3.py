lis = input("Enter numbers separated by space: ").split()
index = 0
while index < len(lis):
    if int(lis[index]) % 3 == 0:
        lis.pop(index)
        index -= 1
    index += 1
print(lis)
