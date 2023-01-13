import time
from random import randint

print("\n\nWELCOME TO GUESS THE NUMBER")
time.sleep(2)
print("YOU WILL GET 3 CHANCES TO GUESS THE NUMBER\n")
time.sleep(3)
print("THE DEFAULT RANGE OF NUMBER IS 1-20")
print("YOU MAY CHANGE THE RANGE LATER")
time.sleep(5)

chance = 3
lower = 1
upper = 20
score = 0


def take_input(text) -> str:
    try:
        res = int(input(text))
        if res < 0:
            raise ValueError
        return res
    except:
        print("\nInvalid input!")
        res = take_input(text)
        return res
    # return res -- DONT


while True:

    while True:
        try:
            print("\n\n0. Exit")
            print("1. Start")
            print("2. Change lower range")
            print("3. Change upper range")
            print("4. Change number of chances")
            print("\nScore:", score, "points.")
            print("Lower:", lower, "| Upper:", upper, "| Chances:", chance)
            choice = int(input("\nEnter your choice: "))
            if 0 > choice > 4:
                raise ValueError
            break
        except:
            print("Please enter a valid choice.")
            continue

    if choice == 0:
        print("Goodbye!")
        break

    elif choice == 2:
        lower_tmp = take_input("Enter lower limit(must be less than upper): ")
        if not lower_tmp < upper:
            print("Lower limit must be less than upper limit(", upper, ")")
            time.sleep(2)
            continue
        lower = lower_tmp
        print("Updated!")
    elif choice == 3:
        upper_tmp = take_input("Enter the upper limit(must be greater than lower): ")
        if not upper_tmp > lower:
            print("Upper limit must be greater than lower limit(", lower, ")")
            time.sleep(2)
            continue
        upper = upper_tmp
        print("Updated!")
    elif choice == 4:
        chance = take_input("Enter number of chances: ")
        print("Updated!")
    elif choice == 1:
        number = randint(lower, upper)
        print("\nNumber has been choosen.\n")
        chance_tmp = chance
        while chance > 0:
            guess = take_input("Enter your guess: ")
            if guess != number:
                print("\nWrong guess! Try again.\n")
                chance -= 1
            else:
                break

        if chance == 0:
            print("You lost!")
            print("Correct number was", number)

        else:
            print("You won!")
            score += 1
        time.sleep(2)
        chance = chance_tmp
        print("Returing to menu")
        time.sleep(2)
