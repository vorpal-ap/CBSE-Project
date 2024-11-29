'''
New stack according to user input
'''


S = []

print("Input 10 numbers")
for i in range(10):
    num = int(input("Enter number: "))
    S.append(num)

print("Stack S: ", S)

print("Choose an option")
print("1 to print multiples of 5")
print("2 to print multiples of 7")
choice = int(input("Choice: "))

if choice == 1:
    new_S = [num for num in S if num % 5 == 0]
    print("New S: ", new_S)
elif choice == 2:
    new_S = [num for num in S if num % 7 == 0]
    print("New S: ", new_S)
else:
    print("Invalid choice")
