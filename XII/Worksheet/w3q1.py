from pickle import load, dump
def countrec():
    count = 0
    file = open("student.dat" , "rb")
    while True:
        try:
            data = load(file)
            if data[2] > 75:
                count += 1
                print("Name: {}, Admission number: {}, Percentage: {}".format(data[1], data[0], data[2]))
        except:
            file.close()
            break
    print("Number of students above 75%:", count)
        
    
countrec()
