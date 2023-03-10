n=int(input())

t=1
while n>1:
    k = n % 10
    n = n // 10
    t*=k
print(t)
