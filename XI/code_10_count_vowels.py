vowels = "aeiouAEIOU"
string = input("Enter a string: ")
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels:", count)
