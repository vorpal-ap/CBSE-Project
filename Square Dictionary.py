'''
Add squares of numbers from 1 to 15 in dictionary
'''


dict = {}
for i in range(1, 16):
    dict.update({i: i*i})
print(dict)
