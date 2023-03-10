a=[1,3,4,5,3,2,4,2,4,4,1,2,3,4,3]
count=[0]*6
for i in a:
    count[i]+=1
print(count)
for i in range(6):
    print(str(i)*count[i], sep=' ')