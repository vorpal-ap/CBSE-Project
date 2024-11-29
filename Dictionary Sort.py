'''
Sort a dictionary
'''



dict = eval(input("Enter dictionary: "))
print("Original dictionary: ", dict)

sort = sorted(dict.items())
sortRev = sorted(dict.items(), reverse=True)

print("Sorted in ascending order: ", sort)
print("Sorted in descending order: ", sortRev)
