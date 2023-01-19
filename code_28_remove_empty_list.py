# lis is the list of lists
lis = []
index = 0
while index != len(lis):
    if lis[index] == []:
        del lis[index]
        index -= 1
    index += 1
print(lis)
