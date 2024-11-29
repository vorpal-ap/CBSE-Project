'''
Add and modify names in stack
'''



Student = []
Student2 = []
for i in range(4):
    Student.append(input("Enter student: "))
print("Input Stack:", Student)
print("Names starting with M: ")
for name in Student:
    if name[0].lower() == 'm':
        print(name)
    if len(name) < 4:
        Student2.append(name)
for name in Student2:
    Student.remove(name)
print("Updated Stack:", Student)
print("Names with less than 4 letters:", Student2)
