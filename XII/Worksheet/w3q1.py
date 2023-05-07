from pickle import load, dump


def countrec() -> None:
    count = 0
    file = open("student.dat", "rb")
    while True:
        try:
            data: tuple = load(file)
            if data[2] > 75:
                count += 1
                print("Name: {1}, Admission number: {0}, Percentage: {2}".format(*data))
        except:
            file.close()
            break
    print("\nNumber of students above 75%:", count)


countrec()
