# l=[1,2,3,4,2,4,5,3,2,3,4,2,3,4]
# count=[0]*6
# for i in l:
#     count[i]+=1
# print(count)

# # n=input()
# n='45523423562898764'
# nlist=list(n)
# lenList=len(nlist)
# maximum=int(max(nlist))+1
# count=[0]*maximum
# for i in nlist:
#     i=int(i)
#     count[i]+=1
# for i in range(maximum):
#     if count[i]>0:
#         print(i,count[i])

import random

n=int(input())
listRand=[]
newList=[0]*201
for i in range(n):
    listRand.append(random.randint(-100,100))
print(listRand)

for i in listRand:
    newList[i+100]+=1

for i in range(201):
    if newList[i]>0:
        print(i-100, end=' ')

