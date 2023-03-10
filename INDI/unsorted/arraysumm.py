a = 19
b = [39, 22, 38, 9, 10, 11, 8]
lenb = len(b)            #  lenb = 7
summ = []
for i in range(lenb):
    for j in range(1,lenb):
        if b[i]+b[j]==a:
            if b[i] not in summ and b[j] not in summ:
                summ.append(b[i])
                summ.append(b[j])
print(summ) #[9, 15, 10, 14, 12, 12]
lenSUM=int(len(summ)/2)
nec=0
cet=1
for i in range(1,lenSUM+1):
    print(summ[nec],summ[cet])
    cet+=2
    nec+=2