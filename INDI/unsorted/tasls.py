# n=int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int, input().split())))
# summ=0
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             summ+=a[i][j]
# print(summ)

# n=int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for j in range(n):
#     for i in range(n):
#
#         print(a[i][j], end='')
#     print()

# n=int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int, input().split())))
# summ=0
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             summ+=a[i][j]
# print(summ)

# n=int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for j in range(n-1,-1,-1):
#     for i in range(n-1,-1,-1):
#
#         print(a[i][j], end='')
#     print()

# n,m=map(int, input().split())  #3
#  #4
# a=[]
#
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for i in range(n):
#     for j in range(m-1,-1,-1):
#         print(a[i][j], end=' ')
#     print()
#
# n,m=map(int, input().split())  #3
#  #4
# a=[]
#
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for i in range(n-1,-1,-1):
#     for j in range(m):
#         print(a[i][j], end=' ')
#     print()
# a = [list(map(int, input().split())) for i in range(5)]
# a=[[0, 0, 1, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0]]
#
# # for i in range(5):
# #     a.append([0]*5)
# for i in range(5):
#     for j in range(5):
#         if a[i][j]==1:
#             n=a.index(a[i])
#             m=a[i].index(a[i][j])
# for i in a:
#     print(i)
# print(n,m)
#
# stepV=abs(n-2)
# stepHor=abs(m-2)
# print(stepHor+stepV)

# n,m=map(int, input().split())
# a=[list(map(int, input().split())) for i in range(n)]
#
# for i in range(n):
#     sumrow=0
#     for j in range(m):
#         sumrow+=a[i][j]
#     print(sumrow, end=' ')
# print()
# for j in range(m):
#     sumcolm = 0
#     for i in range(n):
#         sumcolm+=a[i][j]
#     print(sumcolm, end=' ')

n=int(input())
a=[list(map(int, input().split())) for i in range(n)]
b=[]

for j in range(n-1,-1,-1):
    for i in range(n - 1, -1, -1):
        # b.append(a[i][j])
        print(a[i][j], end=' ')

    print()
    # a[i][j]
    # b[i][j]
# print(a)
# for i in b:a
#     print(i,end=' ')