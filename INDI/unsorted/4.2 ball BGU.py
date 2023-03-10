i = j = 0
maleList = []
femaleList = []
couples = 0
m = int(input())
while len(maleList) < m:
    maleList = list(map(int, input().split()))
f = int(input())
while len(femaleList) < f:
    femaleList = list(map(int, input().split()))
print(maleList, femaleList)
for i in maleList:
    for j in femaleList:
        while 0 <= abs(maleList[i] - femaleList[j]) <= 1:
            couples += 1
            if len(maleList)!=0 or len(femaleList)!=0:
                maleList.remove(i)
                femaleList.remove(j)
print(couples)
