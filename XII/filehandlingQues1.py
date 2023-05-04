VOWELs = "aeiouAEIOU"
def count_c_v():
    with open("data.txt") as file:
        data = file.read()
        vowel = 0
        conso = 0
        for letter in file:
            if letter in VOWELS:
                vowel += 1
            elif letter.isalpha():
                conso += 1

        print("Number of vowels: {}\nNumber of consonants: {}".format(vowel, conso))

if __name__ == "__main__":
    count_c_v()