n = int(input())

while True:
    n+=1
    year = {i for i in str(n)}
    if len(year)==4:
        break
print(n)