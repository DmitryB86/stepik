n = int(input())
strROK = 'рок'
a = []
for i in range(1,n+1):
    stringi = input().lower()
    if strROK in stringi:
       # get index
        pos=stringi.find(strROK)
        if stringi.count(strROK)<2:
            a.append(i)
            a.append(pos + 1)
        else:
            count=stringi.count(strROK)
            for j in range(count):
                pos=stringi.find(strROK)
                a.append(i)
                a.append(pos + 1)
                stringi = stringi[:pos] + 'RRR' + stringi[pos + 3:]
while len(a)>0:
    print(a[0],a[1])
    a=a[2:]