n = int(input())
lenn = len(str(n))

st=str(n).zfill(6)
# print(st,lenn, type(st),type(lenn), sep='___')
# print(st[4],st[0],st[1],type(int(st[0])))

if int(st[0])+int(st[1])+int(st[2])==int(st[3])+int(st[4])+int(st[5]):
    print('YES')
else:
    print('NO')