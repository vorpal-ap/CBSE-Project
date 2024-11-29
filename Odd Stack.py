'''
Create stack of odd numbers
'''



numbers = eval(input("Enter list of numbers: "))
print("Stack =", numbers)
oddStack = [num for num in numbers if num % 2 == 1]
if oddStack:
    print("Odd numbers =", oddStack)
    print("Max odd number =", max(oddStack))
else:
    print("Odd stack is empty")
