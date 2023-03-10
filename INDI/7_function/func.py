# # объявление функции
# def count_letter(text, letter):
#     print(text.count(letter))
#
# # считываем данные
# text = input()
# symbol = input()
# # вызываем функцию
# count_letter(text, symbol)

# def train(a: int, b: int | float | str):
#     pass
#
# def format_name_list(list_d: list) -> str:
#
#     list_s: list[str]=[]
#     for i in list_d:
#         # print(i)
#         for value in i:
#             list_s.append(i[value])
#
#     if len(list_s)==0:
#         return ''
#     elif len(list_s)==1:
#         return list_s[0]
#     elif len(list_s) == 2:
#         return list_s[0]+' и '+list_s[1]
#     elif len(list_s)>2:
#         s_end = list_s[-2] + ' и ' + list_s[-1]
#         s_begin = list_s[:-2]
#         return ', '.join(s_begin)+', '+s_end

#
# list_e = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]
# # list_e = [{'name': 'Bart'}, {'name': 'Lisa'},{'name': 'Maggie'}]
# # list_e = [{'name': 'Bart'}]
# # list_e=[]
# ''''''
# print(format_name_list(list_e))
from typing import Any
def first_repeated_word(st:str) -> str:
    '''Находит первый дубль в строке'''
    s_t = []
    list_s = [word for word in s.split()]
    for word in s.split():
        if word not in s_t:
            s_t.append(word)
    len_st = len(s_t)
    if len_st!=len(s.split()):
        return list_s[len_st]

# s = "ab ca bc ab"
# s='ab ca bc Ab cA aB bc'
# s = 'ab ca bc ca ab bc'
s="ab ca bc"
print(first_repeated_word(s))


# def factorial(n):
#     rez=1
#     for i in range(rez, n):
#         rez+=rez*i
#     return rez
#
# def trailing_zeros(n):
#     st = str(factorial(n))
#     count=0
#     while st[-1] == '0':
#         count+=1
#         st = st[:-1]
#     return count
#
# print(trailing_zeros(10))
