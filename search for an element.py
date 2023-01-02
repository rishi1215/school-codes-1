n = int(input("Enter number of elements: "))

lis = []
for _ in range(n):
    lis.append((input("Enter element: ")))
search = input("Enter the value to search for: ")
print()
while n>0:
    element = lis[n-1]
    if element == search:
        print("Found element at index ", n-1)
    n-=1
if search not in lis:
    print("Element is not in list.")