'''
Print number of odd and even numbers in a given tuple
'''

def tupleCount(tup):
    odd, even = 0, 0
    for i in tup:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Odd = ", odd)
    print("Even = ", even)


tup = eval(input("Enter tuple: "))
tupleCount(tup)
