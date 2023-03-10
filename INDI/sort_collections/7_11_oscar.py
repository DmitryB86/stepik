oscar_n = int(input())
dict_oscar = dict()
for i in range(oscar_n):
    actors = input()
    if actors in dict_oscar:
        dict_oscar[actors]+=1
    else:
        dict_oscar[actors] = 1

mina = min(dict_oscar.items(), key=lambda x: x[1])
maxa = max(dict_oscar.items(), key=lambda x: x[1])
print(f'{maxa[0]}, {maxa[1]}')
print(f'{mina[0]}, {mina[1]}')
# max = sorted(dict_oscar(), key=lambda  )