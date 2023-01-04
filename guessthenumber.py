import time
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

while True:
    while True:
        try:
            print("\n\n0. Exit")
            print("1. Start")
            print("2. Change lower range")
            print("3. Change upper range")
            print("4. Change number of chances")

            choice = int(input("\nEnter your choice: "))
            if choice > 4:
                raise ValueError
        except:
            print("Please enter a valid choice.")
        break
