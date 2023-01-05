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
    except:
        print("\nInvalid input!")
        take_input(text)

while True:


    while True:
        try:
            print("\n\n0. Exit")
            print("1. Start")
            print("2. Change lower range")
            print("3. Change upper range")
            print("4. Change number of chances")
            print("\nScore: ", score, " points.")

            choice = int(input("\nEnter your choice: "))
            if choice > 4:
                raise ValueError
            break
        except:
            print("Please enter a valid choice.")
            continue
    
    if choice == 0:
        print("Goodbye!")
        break

    elif choice == 2:
        try:
            pass
        except:
            pass

    elif choice == 3:
        pass

    elif choice == 4:
        pass
    
    elif choice == 1:
        number = randint(lower, upper)
        print("\nNumber has been choosen.\n")

        while chance>0:
            guess = take_input("Enter your guess: ")
            if guess != number:
                print("\nWrong guess! Try again.\n")
                chance -= 1
            else:
                break

        if chance==0:
            print("You lost!")
            print("Correct number was ", number)
            
        else:
            print("You won!")
            score += 1
        time.sleep(2)
        print("Returing to menu")
        time.sleep(2)