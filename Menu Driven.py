'''
Menu driver program on numbers
'''


number = int(input("Enter number: "))

print("Press 1 to reverse a number")
print("Press 2 to check if a number is palindrome")
print("Press 3 to print sum of digits of a number")
choice = int(input("Enter choice: "))

if choice == 1:
    print("Reverse of", number, "is", int(str(number)[::-1]))

if choice == 2:
    if number == int(str(number)[::-1]):
        print(number, "is a palindrome number")
    else:
        print(number, "is not a palindrome number")

if choice == 3:
    sum = 0
    for digit in str(number):
        sum += int(digit)
    print("Sum of digits of", number, "is", sum)
