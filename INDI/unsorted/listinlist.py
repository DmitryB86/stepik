# a=[[1,2,3,5],
#    [4,5,6,7],
#    [9,8,4,3]]
# # b=['hello','hi','world']
# # for i in a:
# #     for j in i:
# #         print(j, end='')
# #     print()
# # for i in range(3):
# #     s=0
# #     for j in range(4):
# #         s=s+a[i][j]
# #     print(s)
a=[]
n=int(input())

for i in range(n):
    a.append([0]*n)


for i in range(n):
    for j in range(n):
        if i==j:
            a[i][j]=10
        elif i>j:
            a[i][j]=5
        else:
          a[i][j]= 8
for i in a:
    print(i)