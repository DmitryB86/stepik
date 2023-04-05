l = [100, 55, 77, 55, 89]
d = {}
i=-1
while len(l)>2:
    d[l[i-1]]=l[i]
    i=i-1
print(d)