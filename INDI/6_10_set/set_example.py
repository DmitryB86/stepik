# my_list = [56, 59, 53, 75, 62, 61, 75, 65, 59, 62, 64, 53,
#            54, 62, 69, 53, 55, 62, 54, 66, 55, 57, 58, 75,
#            72, 55, 51, 56, 71, 66, 57, 56, 59, 73, 68, 57,
#            50, 54, 62, 68, 59, 64, 59, 59, 71, 68, 57, 54, 53, 72]
#
#
# my_list=list(set(my_list))
# l = len(my_list)
# s = sum(my_list)
# print(s/l)

# name = input()
# name_len = len(set(name))
# if name_len%2!=0:
#     print('IGNORE HIM!')
# else:
#     print('CHAT WITH HER!')

# a,b,c,d = map(int, input().split())
# s = set()
# s.update([a,b,c,d])
# print(4-len(s))
# al = range('a','z')
#
# alphabet = set(['a-z'])
# print(alphabet)
# print(al)

# import string
# alpha_set = set(string.ascii_lowercase)
# print(string.ascii_lowercase)
# st = input()
# st_set = set(st.lower())
# if alpha_set == st_set:
#     print('YES')
# else:
#     print('NO')


# alpha_set = set('abcdefghijklmnopqrstuvwxyz')
# st = input().lower()
# st_set = set(st)
# if alpha_set == st_set:
#     print('YES')
# else:
#     print('NO')

# s=input()
#
# s = s[1:-1].replace(', ', '')
# print(len(set(s)))


# set_a = {31, 37, 39, 41, 47, 58, 60, 62, 70, 75,
#          76, 77, 78, 79, 80, 81, 85, 86, 88, 90, 93, 96, 98, 99}
#
# set_b = {0, 1, 8, 16, 17, 18, 22, 24, 29, 31,
#          33, 34, 36, 42, 46, 47, 51, 53, 62, 64, 65, 66, 67}
# print(len(set_a ^ set_b))

# print(str([chr(i) for i in range(ord('A'),ord('Z'))]))
# words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
#          'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',
#          'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
#          'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
#          'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention', 'tradition',
#          'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal', 'government',
#          'control', 'value', 'few', 'generation', 'service', 'national',
#          'tradition', 'government', 'mention', 'proposal']
# words_set= set(words)
# count=0
# for i in words_set:
#     if len(i)>6:
#         count+=1
# print(count)

    n=int(input())
    # set_list = []
    sum_set = set()
    for i in range(n):
        set_in = set(input().split())
        sum_set.update(set_in)
        # set_list.append(set_in)
    print(len(sum_set))
# len_set_list = len(set_list)
# sum_set = set()
# for i in range(len_set_list):
#     sum_set = i&(i+1)
# print(sum_set)