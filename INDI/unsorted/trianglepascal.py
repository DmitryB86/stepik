# n=int(input())
# triangle=[]
#
# for i in range(n+1):
#     triangle.append([1]+[0]*n)
# # for i in triangle:
# #     print(i)
#
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         triangle[i][j]=triangle[i-1][j]+triangle[i-1][j-1]
#
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(triangle[i][j], end=' ')
#     print()
import random


# a=[(i,j,k) for i in 'asfgr' for j in [1,2,3] for k in 'drw']
# print(a)
# zeroes=[int('0') for i in range(100)]
# print(zeroes)

# n=int(input())
# # a=[i for i in range(1,n+1) if n%i==0 ]
# # print(a)
# a=[i for i in range(n, n**2+1) if i%2!=0]
# print(a)

# n,m=map(int, input().split())
# if n<=m:
#     a = [i**2 for i in range(n,m+1)]
# else:
#     a = [i**3 for i in range(n,m-1,-1)]
#
# print(a)
# str='hello world my beautifull piecfull place in Egypt'
# a=[i[0] for i in str.split()]
# print(a)

# from string import ascii_uppercase
#     # n=int(input())
# n=3
#
# # for i in st:
# #     print(i)
#
# a=[i*(ord(i)-64) for i in list(ascii_uppercase)[:n] ]
#
# print(a) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ

# phrase = 'Take only the words that start with t in this sentence'
# # print(phrase.split())
# a=[i for i in list(phrase.split()) if i[0] in ('T','t')]
# print(a)
# k=None
# i_love_none=[k]*50
# print(i_love_none)
# my_tuple = (
# 32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45,
# 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34,
# 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68,
# 56, 26, 39, 34, 50, 10, 12, 3, 27)
#
# slice_5_10 = my_tuple[5:11]
# slice_from_20 = my_tuple[20:]
# slice_to_35 = my_tuple[5:35]
#
# print(slice_5_10)
# print(slice_from_20)
# print(slice_to_35)
# my_tuple = (32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45, 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34, 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68, 56, 26, 39, 34, 50, 10, 12, 3, 27)
#
# print(my_tuple[::-1])

# words_tuple = ('quaint', 'leftovers', 'thesis', 'density', 'retired', 'weak', 'tolerate',
#                'sensitivity', 'primary', 'definition', 'determine', 'bring', 'monstrous',
#                'hurl', 'timetable', 'month', 'advocate', 'provoke', 'stress', 'omission')
# for i in words_tuple:
#     len_word = len(i)
#     print(f'Длина слова {i} = {len_word}')
my_tuple = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
summ=0
cnt=0
for i in my_tuple:
    if i%2!=0:
        summ+=i
        cnt += 1
print(summ/cnt, cnt)
