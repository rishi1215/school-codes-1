from pickle import load


def createSampleData() -> None:
    import random
    from pickle import dump
    file = open("doctors.dat", "wb")
    names = ["Arun", "Bhaskar", "Chandru", "Dinesh", "Eswar", "Fayaz", "Ganesh", "Hari", "Irfan", "Jagan"]
    for i in range(10):
        dump([i, "Dr. " + random.choice(names)], file)


def details(n) -> None:
    try:
        file = open("doctors.dat", "rb")
    except FileNotFoundError:
        choice = input("File not found! Create sample data? (y/n): ")
        if choice == "y":
            createSampleData()
            file = open("doctors.dat", "rb")
        else:
            return
    while True:
        try:
            doctor = load(file)
            if doctor[0] == n:
                print("Doctor ID:", doctor[0])
                print("Doctor Name:", doctor[1])
                break
        except EOFError:
            print("Doctor not found!")
            break
        
details(int(input("Enter doctor ID: ")))