# mas = [2, 3, 3, 9, 5, 6, 7, 4]
# for run in range(len(mas) - 1):
#     for i in range(len(mas) - 1-run):
#         while mas[i] > mas[i + 1]:
#             mas[i], mas[i + 1] = mas[i + 1], mas[i]
#
# print(mas)

n=6
mas = [3,1,8,4,7,2]
for j in range(1,n):
    key = mas[j]
    i=j-1
    while i>=0 and mas[i]>key:
        mas[i+1]=mas[i]
        i=i-1
    mas[i+1]=key
print(mas)

kkk={}
kkk.setdefault()