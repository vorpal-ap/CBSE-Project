'''
Check if number is Buzz number
'''


number = int(input("Enter number: "))
if number % 10 == 7 or number % 7 == 0:
    print(number, "is a Buzz number")
else:
    print(number, "is not a Buzz number")
