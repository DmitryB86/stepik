s=input()
store=[]
m=[]
for s1 in s:
    for s2 in s:
        for s3 in s:
            for s4 in s:
                m=[s1]+[s2]+[s3]+[s4]
                store.append(m)
                store.sort()
for i in store:
    print(i,end='')
