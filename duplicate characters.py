str1 = input("Enter a string: ").lower()
dups = []
for i in str1:
    if str1.count(i) > 1 and i not in dups:
        dups.append(i)
if dups:
    print("List of duplicate characters: ", dups)
else:
    print("There are no duplicate characters")