'''
Add record to binary file
'''


import pickle

def createFile():
    file = open('Book.dat', 'ab')
    bookNo = int(input("Enter book number: "))
    bookName = input("Enter book name: ")
    author = input("Enter author: ")
    price = int(input("Enter price: "))
    record = [bookNo, bookName, author, price]
    pickle.dump(record, file)
    print("Added record")
    file.close()


createFile()

