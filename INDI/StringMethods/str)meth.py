# def check_sum(*args: int):
#
#     if sum(args)<50:
#         print('not enough')
#     else:
#         print('verification passed')
# check_sum(8,1,2,3)

# def multiply(*args: int):
#     s=1
#     for i in args:
#         s*=i
#     print(s)
# multiply()
# THIS TASK IS NOT FINISHED
# def only_one_positive(*args):
#     count=0
#     for i in args:
#         if i>0 and len(args)>1:
#             count+=1
#     return (count==1)
#
# only_one_positive()

# def print_goods(*args):
#
#     d={}
#     n=1
#     for i in args:
#         if type(i)!=str:
#             continue
#         else:
#             if len(i)<1:
#                 continue
#             else:
#                 d[f'{n}.']=i
#                 n+=1
#     if len(d)==0:
#         print('Нет товаров')
#     else:
#         for key,value in d.items():
#             print(key,value)

# print_goods(True,1,5,'apple', 'banana', 'orange',1,2,[1,2,],'')
# print(print_goods(1,2,[1,2,],''))

# def info_kwargs(**kwargs):
#     for para in sorted(kwargs):
#         print(f'{para} = {kwargs[para]}')
#
# info_kwargs(first_name="John", last_name="Doe", age=33)

# def polindrom(s):
#     if len(s)<=1:
#         return True
#     if s[0]!=s[-1]:
#         return False
#     return polindrom(s[1:-1])
#
#
# print(polindrom('шалаш'))

# def print_from(n: int) -> None:
#     if n>0:
#         print(n)
#         return print_from(n-1)
#
# print_from(10)
#
# def print_to(n: int) -> None:
#     if n==0:
#         return
#     print_to(n-1)
#     print(n)
#
# print_to(6)

# def reverse_rec(n: int, st: str) ->str:
# def print_from(n: int):
#
#     if n>0:
#         print_from(n-1)
#         print(list_n[-n], end = " ")
#
# n=int(input())
# list_n = list(map(int, input().split()))
# print_from(n)

# def double_fact(n):
#     '''Find dounle factodial '''
#     if n==1:
#         return 1
#     if n==2:
#         return 2
#     return double_fact(n-2)*n
#
# print(double_fact(6))

# def tribonacci(a):
#     ''' Find number of Tribonachi'''
#     if a==0:
#         return 0
#     if a==1:
#         return 0
#     if a==2:
#         return 1
#     return tribonacci(a - 1) + tribonacci(a - 2) + tribonacci(a - 3)
#
# a=int(input())
# print(tribonacci(a))

# def get_combin(n,k):
#     if k==0:
#         return 1
#     if k==n:
#         return 1
#     return get_combin(n-1,k)+get_combin(n-1,k-1)
#
# n = int(input())
# k = int(input())
# print(get_combin(n, k))

# def ackermann(m,n):
#     if m==0:
#         return n+1
#     if n==0:
#         return ackermann(m-1,1)
#     return ackermann(m-1,ackermann(m,n-1))
# m = int(input())
# n = int(input())
# print(ackermann(m,n))

# def list_sum_recursive(n):
#     s=0
#     if n==0:
#         return
#
#     list_sum_recursive(n-1)
#     s=s+ls[n]
#     return s
#
# ls=list(map(int, input().split()))
# s = 0
# print(list_sum_recursive(len(ls)-1))

def rec(s):
    if len(s) ==1 or len(s)==2:
        return s
    return s[0]+'(' +rec(s[1:-1])+ ')' +s[-1]

s='kjg;lkdsjglksjgkdsjg;ldfnjglkd'
print(rec(s))