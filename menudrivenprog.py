# Menu driven program
from colorama import Fore, Style
choice = None

choice0 = "0. Exit"
choice1= "1. Add employee"
choice2 = "2. Show all employee"
choice3 = "3. Delete employee" 

for i in range(1):
    print(Fore.CYAN + " -------------WELCOME-------------")
    print(Fore.GREEN + """          {}
{}
{}    
""")
    choice = int(input(Fore.WHITE + "Please enter your choice: "))

