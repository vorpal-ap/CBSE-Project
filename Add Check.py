'''
Add record and check author
'''

import pickle

def createFile():
    fileWrite = open('Book.dat', 'ab')
    bookNo = int(input("Enter book number: "))
    bookName = input("Enter book name: ")
    author = input("Enter author: ")
    price = int(input("Enter price: "))
    record = [bookNo, bookName, author, price]
    pickle.dump(record, fileWrite)
    print("Added record")
    fileWrite.close()


def countRec(author):
    fileRead = open('Book.dat', 'rb')
    count = 0
    try:
        while True:
            record = pickle.load(fileRead)
            if record[2] == author:
                count += 1
    except EOFError:
        pass
    fileRead.close()
    return count


createFile()
author = input("Enter author to find: ")
print("Books by author: ", countRec(author))
