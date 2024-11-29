'''
Add employee records to file
'''


import pickle

count = 1
try:
    with open('employee.dat', 'rb') as file:
        try:
            while True:
                record = pickle.load(file)
                count = record[0] + 1
        except EOFError:
            pass
except FileNotFoundError:
    pass

read = True

with open('employee.dat', 'ab') as file:
    while read:
        data = [count]
        employeeName = input("Enter employee name: ")
        data.append(employeeName)
        basicSalary = int(input("Enter basic salary: "))
        data.append(basicSalary)
        allowances = int(input("Enter allowances: "))
        data.append(allowances)
        totalSalary = basicSalary + allowances
        data.append(totalSalary)
        print(data)
        loopInput = input("Add another record (y/n): ")
        if loopInput.lower() == 'n':
            read = False
        count += 1
        pickle.dump(data, file)

with open('employee.dat', 'rb') as file:
    try:
        while True:
            record = pickle.load(file)
            print("Record number: ", record[0])
            print(record)
    except EOFError:
        pass
    print("Size of file = ", file.tell())
    
