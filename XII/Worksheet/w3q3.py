from pickle import load, dump
from re import findall


def createSampleData() -> None:
    import random

    items: list[str] = [
        "Apple",
        "Banana",
        "Orange",
        "Grapes",
        "Mango",
        "Pineapple",
        "Watermelon",
        "Papaya",
        "Guava",
        "Kiwi",
    ]
    file = open("items.dat", "wb")
    for i in range(10):
        data = {"Item": items[i], "Price": random.randint(10, 100)}
        dump(data, file)
    file.close()
    print("Sample data created successfully")


def FindAverage():
    try:
        file = open("items.dat", "rb")
    except FileNotFoundError:
        input = input("File not found, create sample data? (y/n): ")
        if input.lower() == "y":
            createSampleData()
            file = open("items.dat", "rb")
        else:
            return
    total = 0
    items = 0
    while True:
        try:
            data: dict = load(file)  # type: ignore
            total += data["Price"]
            items += 1
            print(data)
        except Exception as e:
            break
    file.close()
    avg: float = round(total / items, 3)
    print("Average price of items is:", avg)


FindAverage()
