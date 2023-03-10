# def file_read(file_name):
#     file = open(file_name, encoding='utf-8')
#     print(file.read())
#
#
# file_read('123.txt')

# def file_n_lines(file_name: str, n: int) -> None:
#     file = open(file_name, encoding='utf-8')
#     for row in range(1,n+1):
#         print(file.readline().strip())
#
# file_n_lines('123.txt',3)

# def create_file_with_numbers(n):
#     file = open(f'range_{n}.txt','a+')
#     for i in range(1,n+1):
#         file.write(f'{i}\n')
#     file.close()
#
# create_file_with_numbers(6)

from pprint import pprint
def remove_punc(word):
    from string import punctuation
    for i in punctuation:
        if i in word:
            word = word.replace(i, '')
    return word

def longest_word_in_file(file_name):
    dic_w = {}
    max_w = ''
    file = open(file_name, encoding='utf-8')
    for row in file:
        for element in row.split():
            element = remove_punc(element)
            if len(element)>len(max_w):
                max_w=element


    print(max_w)


longest_word_in_file('123.txt')
