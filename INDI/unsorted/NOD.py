a, b=map(int,input().split())
n,m=a,b
while b>0:
    a,b=b,a%b
    c=a
print(c)

nok=n*m/c
print(nok)