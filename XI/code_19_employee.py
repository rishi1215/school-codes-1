Names = []
Salary = []
emp_dict = {"empname": Names, "salary": Salary}
choice = 1
while choice != 0:
    print("1. Add Employee Detail ")
    print("2. Show All Employee Detail ")
    print("3. Search Employee ")
    print("0. Quit ")
    choice = int(input("Enter your choice :"))
    if choice == 1:
        name = input("Enter name")
        salary = int(input("Enter Salary "))
        Names.append(name)
        Salary.append(salary)
    elif choice == 2:
        if not Names:
            print("\nNo records to show.\n")
            continue
        print("************** EMPLOYEE DETAILS ***************")
        print("%20s" % "NAME", "%10s" % "SALARY")
        print("----------------------------------------------------")
        n = emp_dict["empname"]
        s = emp_dict["salary"]
        for i in range(len(n)):
            print("%20s" % n[i], "%10s" % s[i])
            print("----------------------------------------------------")
    elif choice == 3:
        print("Enter name to search: ")
        name = input("Enter name")
        n = emp_dict["empname"]
        s = emp_dict["salary"]
        try:
            pos = n.index(name)
            print("## Record Found ##")
            print("Salary :", s[pos])
        except:
            print("Name not in the record ")
