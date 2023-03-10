# file = open('passw.txt', 'w')
# file.write([1,2,3,4])
# file.close()

# with open('passw.txt','w') as f:
#     f.write('one two three four')
#     f.write('five six seven')
# # print('end')
#
# import os
# with os.scandir(r'E:\\') as entries:
#     for entrie in entries:
#         print(f'{entrie.name} -> {entrie.stat().st_size} bytres')

# def find_lines_len_more_6(file_name:str) -> int:
#     count_st=0
#     with open(file_name, 'r', encoding='utf-8') as f:
#         rows = f.readlines()
#         for row in rows:
#             if len(row.strip())>6:
#                 count_st+=1
#     return count_st


# def uniq(file_name: str) ->int:
#
#     with open(file_name, 'r', encoding='utf-8') as file:
#         # count_uniq = 0
#         ll=[]
#         rows = file.readlines()
#         for row in rows:
#             for word in row.split():
#                 word = word.lower()
#                 # if row.split().count(word) not in ll:
#                 if word not in ll:
#                     ll.append(word)
#                     # count_uniq+=1
#                 # print(word, len(word),type(word))
#         return len(ll)
#
#
# print(uniq('lorem.txt'))
# # print(uniq('lorem1.txt'))
# from pprint import pprint
# def count_in_dict(file_name: str) -> dict:
#     with open(file_name, 'r', encoding='utf-8') as f:
#         dict_word={}
#         rows = f.readlines()
#         for word in rows:
#             for element in word.split():
#                 element = element.upper()
#                 if element in dict_word:
#                     dict_word[element]+=1
#                 else:
#                     dict_word[element] = 1
#     return dict_word
#
#
# print(count_in_dict('lorem.txt'))
from pprint import pprint
from operator import itemgetter
def find_uniq(file_name: str) -> list:
    set_word= set()
    dict_ser = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        rows = f.readlines()
        for row in rows:
            row = row.strip().upper()
            if row[-2:]=='ЕЯ':
                set_word.add(row)
        for elem_set in set_word:
            dict_ser[elem_set]=len(elem_set)
        sort_dic = sorted(dict_ser.items(), key = lambda item:item[1])
        for elem in sort_dic:
            print(elem[0])

find_uniq('words.txt')