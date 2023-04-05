n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int, input().split())))
count=0
for i in range(n):
    for j in range(n):
        if i!=j and a[i][j]==a[j][i]:
            count+=1
if count ==n*n-n:
    print('Yes')
else:
    print('No')

