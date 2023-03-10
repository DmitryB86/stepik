#
# summ=0
# for i in range(1000,10000):
#     if (i%10+(i//10)%10+(i//100)%10 +i//1000)==20:
#         summ=summ+i
#         # print(i,i%10,(i//10)%10,(i//100)%10 ,i//1000,type(i//1000))
# print(summ)

# # n=int(input())
# n=3
# for i in range(1,n+2):
#    for j in range(1,i):
#         print(j,end='')
#    print()

# def nn(a,b):
#     n=a**2+b
#     return n
# def mm(a,b):
#     m=b**2+a
#     return m
# n,m=map(int, input().split())
# count=0
# for i in range(0,n+1):
#     for j in range(0,m+1):
#          if mm(i,j)==m and nn(i,j)==n:
#              count+=1
# print(count)
#

n=int(input())
count = 0
i = 1
for k in range(n,2*n):
    for i in range(1,k+1):
        if k % i == 0:
            count += 1
            # print(k,count)
        i += 1
    if count<=2:
        print(k,count)

    count = 0
# print(count)
