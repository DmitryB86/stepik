# s='as As sdf df dkcr as sdf DF'
# b=list(s.upper().split())
# c=b[0]
# count=0
# d={}
# for i in range(len(b)):
#     if c==b[i]:
 #инициализация строки
 n = str(input())
# n='a aa abC aa ac abc bcd a'
m = [] #инициализация списка
m.append(str(s.lower()) for s in n.split())
d = {} #инициализация пустого словаря
lj = len(m[0])
# for i in range(li):
    for j in range(lj):
        p = m[j]
        if p in d:
            d[p]+=1
        else:
            d[p] = 1
for key,value in d.items():
   print(key,value)