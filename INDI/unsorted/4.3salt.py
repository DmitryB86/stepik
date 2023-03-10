# 5
# лук соль перец
# картофелин штук 3
# картошку пожарить и поперчить
# сварить морковь и добавить соль
# сварить суп

n=int(input())
recepie=str()
for i in range(n):
    s=input()
    if 'соль' in s:
        continue
    else:
        recepie+=s+', '
print(recepie[:-2])