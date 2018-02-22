

fileName = str(input('Γράψε όνομα αρχείου : '))
numwords=0
numLines=0
fileToRead = open(fileName, 'r') # 'r' reads the file
# print(fileToRead.read()) # reading file
# fileToRead.close() # closing the file
# lekseis=(fileToRead.read()).split()
# print(lekseis)
with open(fileName) as f:
    data = f.read()
foula=data.split()
# print(foula)
words=foula
peza=[word for word in words if word.islower()]
print(peza)
number_of_words=len(peza)
print(number_of_words)
# with open (fileName) as f:
#     data = f.read()
#     for line in fileName:
#         wordList = line.split()
#         numwords += len(wordList)
# print(numwords)
# print(peza[0],peza[1],peza[2])
# n=1
# i=1
mylist=[peza]
print(mylist])

import random
print(random.choice(peza))
# μέχρι αυτό το σημείο κατάφερα να το φτάσω κ.Πατσάκη.
