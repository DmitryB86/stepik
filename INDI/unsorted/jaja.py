# def is_person_teenager(age):
#     return 12<=age<=17

# def factorial(a):
#     pr=1
#     for i in range(2, a+1):
#         pr=pr*i
#     return pr

# def generate_fizz_buzz_list(n):
#     mas=[]
#     for i in range(1, n+1):
#         if i%3==0 and i%5==0:
#             mas.append('FizzBuzz')
#         elif i%3==0:
#             mas.append('Fizz')
#         elif i % 5 == 0:
#             mas.append('Buzz')
#         else:
#             mas.append(i)
#     return mas
# print(generate_fizz_buzz_list(10))
# gcd(a,b,c,d)=gcd(a,b)
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
#
# n = int(input())
# mas = []
# while n != 0:
#     nums = int(input())
#     mas.append(nums)
#     n -= 1
#     # НОД(a, b, c,d) = НОД(НОД(НОД(a, b), c),d)
# for i in mas:
#     while len(mas) !=1:
#         mas.append(gcd(mas[0], mas[1]))
#         mas = mas[2:]
# print(mas)
#
#
# def find_duplicate(spisok):
#     nodubl = []
#     for i in spisok:
#         if spisok.count(i)>1 and i not in nodubl:
#             nodubl.append(i)
#     return nodubl
#
#
# spisok = [1, 2, 3, 4]
#
#
# print(find_duplicate(spisok))
# def first_unique_char(st):
#
#     indexST = 0
#     for i in st:
#         if st.count(i) == 1:
#             indexST = st.index(i)
#             break
#         else:
#             indexST = -1
#     return indexST
# st=input()
# print(first_unique_char(st))
# st=input()
#
# for i in st.split():
#     print('*'*int(i))



# n=int(input())
# count = 0
# i = 1
# # for k in range(n,2*n):
# k = 10001
# for i in range(1, k + 1):
#     if k % i == 0:
#         count += 1
#         # print(k,count)
#     # i += 1
# if count <= 2:
#     print(k, count)
#
# count = 0
# # print(count)

# n=int(input())
# # listn=[map(int, input().split()) if len(lis)<]
# listn=[]
# while n>0:
#     nums=int(input())
#     listn.append(nums)
#     n-=1
listn = [34, 23, 12, 28, 23, 34,1,2,8,3,5,2,6]
l=len(listn)
for i in range(l):
    while listn[i]>listn[i+1]:
        listn[i],listn[i+1]==listn[i+1],listn[i]
        # listn.index(listn[i])
        # listn.index(listn[i + 1])
        # listn.remove(listn[i])
        # listn.remove(listn[i+1])
        # listn.insert(listn.index(listn[i]), listn[i+1])
        # listn.insert(listn.index(listn[i + 1]),listn[i])

print(listn)