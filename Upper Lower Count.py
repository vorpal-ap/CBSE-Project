'''
Count number of UPPERCASE and lowercase characters in a string
'''

def Count(string):
    dict = {"uppercase": 0, "lowercase": 0}
    for i in string:
        if i.isupper():
            dict["uppercase"] += 1
        if i.islower():
            dict["lowercase"] += 1
    print("Uppercase = ", dict["uppercase"])
    print("Lowercase = ", dict["lowercase"])

