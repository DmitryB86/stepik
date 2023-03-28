import random

l = random.sample(range(10, 30), 5)
print(l)
d =dict()
for i in l:
    for k,v in d.items():
        k=(i-1)
        v=i

    # d[i-1]=i

print(d)