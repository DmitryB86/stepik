a = list(map(int, input().split()))

c = [i for i in a if i not in [3,5,7,9]]

print(c)