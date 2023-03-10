n = int(input())
i = 1
a=[]
summ=0
while i*i <= n:
    if n % i == 0:
        if i==n//i:
            a.append(i)
        else:
            a.append(i)
            a.append(n//i)
    i += 1
print(a)
for j in a:
    summ+=j
print(summ)