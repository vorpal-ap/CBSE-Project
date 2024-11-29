'''
Count sentences not starting with T
'''

def checkT(sentence):
    return sentence[0].lower() != 't'


count = 0
file = open('Story.txt', 'r')
sentences = file.readlines()
for sentence in sentences:
    if checkT(sentence) and sentence != "\n":
        count += 1
print(count)
