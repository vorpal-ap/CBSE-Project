'''
Count number of words ending with e
'''


file = open('article.txt', 'r')
count = 0
wordList = file.read().split(' ')
for word in wordList:
    if word[-1] == 'e':
        count += 1
print("Words ending with e = ", count)
