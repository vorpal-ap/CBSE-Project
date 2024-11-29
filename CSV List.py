'''
Add and print list in csv
'''

import csv

data = eval(input("Enter list: "))

with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data)
with open('file.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
