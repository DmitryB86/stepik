n,m = map(int, input().split())
l = (list(map(int, input().split())) for _ in range(n))
final_l = []
for index, value in enumerate(l):
    final_l.append((sum(value),index))
print(*max(final_l, key= lambda a:a[0]), sep='\n')
