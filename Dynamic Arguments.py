'''
Sum and Product of numbers using dynamic arguments
'''

def Sum(*args):
    sum = 0
    for i in args:
        sum += i
    print("Sum = ", sum)


def Product(*args):
    product = 1
    for i in args:
        product *= i
    print("Product = ", product)

