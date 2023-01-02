
print("Write `DONE` when done inputting all elements")
l = []
while True:
    _ = input("")
    if _ == "DONE":
        break
    l.append(_)
check = input("Which element to count for? ")
count = 0
for _ in l:
    if check == _:
        count += 1
print(f"Number of occurence of  {check} is {count}")