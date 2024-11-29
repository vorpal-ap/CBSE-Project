'''
Add and print numbers in binary file
'''


import pickle

with open('binary.dat', 'wb') as file:
    read = True
    while read:
        num = int(input("Enter number: "))
        pickle.dump(num, file)
        if input("Do you want to enter another number (y/n): ").lower() == 'n':
            read = False

with open('binary.dat', 'rb') as file:
    try:
        while True:
            data = pickle.load(file)
            print(data)
    except EOFError:
        pass
    
