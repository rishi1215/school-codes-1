from pickle import load


def createSampleData():
    import random
    from pickle import dump

    file = open("bus.dat", "wb")
    for i in range(10):
        # bus = [BusId, start, destination]

        place1 = random.choice(
            ["Cochin", "Trivandrum", "Calicut", "Kannur", "Kasargod"]
        )
        place2 = random.choice(
            ["Cochin", "Trivandrum", "Calicut", "Kannur", "Kasargod"]
        )
        while place1 == place2:
            place1 = random.choice(
                ["Cochin", "Trivandrum", "Calicut", "Kannur", "Kasargod"]
            )

        bus = [random.randint(1, 100), place1, place2]
        dump(bus, file)
    file.close()
    print("Sample data created")


def SearchDestination():
    try:
        file = open("bus.dat", "rb")
    except FileNotFoundError:
        choice = input("Sample data not found. Create sample data? (y/n): ")
        if choice.lower() == "y":
            createSampleData()
            file = open("bus.dat", "rb")
        else:
            return

    while True:
        try:
            bus = load(file)
            if bus[2] == "Cochin":
                print("Bus ID: {0}, Starting Point: {1}, Destination: {2}".format(*bus))
        except EOFError:
            file.close()
            break


SearchDestination()
