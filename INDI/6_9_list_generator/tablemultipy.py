tablemul = [1,2,3,4,5,6,7,]
tablemul1 = [8,2,4,5,7,4]
d=[]
for i in tablemul:
    for j in tablemul1:
        if i not in d and j not in d:
            d.append(i)
            d.append(j)
print(d)