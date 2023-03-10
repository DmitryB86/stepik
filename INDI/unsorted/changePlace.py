s='папа вышел купить арбуз для семьи'
#   папа вышел для арбуз купить семьи
change='2 4'.split()
slist=s.split()
firstWord = int(change[0]) #2
secondW = int(change[1])   #4
firstWorM=slist[firstWord]
secondWorM=slist[secondW]
# print(firstWord, firstWorM, secondW, secondWorM)
slist.remove(firstWorM)
slist.remove(secondWorM)
slist.insert(firstWord,secondWorM)
slist.insert(secondW,firstWorM)

# +s[firstWord]+s[secondW:]
print(*slist)