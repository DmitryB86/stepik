# def get_domain_name(url):
#
#     if '//' in url:
#         if 'www.' in url:
#             url = url[url.find('//')+6:]
#         else:
#             url = url[url.find('//')+2:]
#     elif 'www.' in url:
#         url = url[4:]
#     if '.' in url:
#         url = url[:url.find('.')]
#     return url
#
#
# print(get_domain_name("http://google.com"))
# print(get_domain_name("https://youtube.com"))
# print(get_domain_name("http://www.zombie-bites.com"))
# print(get_domain_name("www.xakep.ru"))

def count_AGTC(dna):
    rez_tuple = (dna.count('A'),dna.count('G'),dna.count('T'),dna.count('C'))
    return rez_tuple

# код ниже не стоит удалять, он нужен для проверки
# assert count_AGTC('AGGTC') == (1, 2, 1, 1)
# assert count_AGTC('AAAATTT') == (4, 0, 3, 0)
# assert count_AGTC('AGTTTTT') == (1, 1, 5, 0)
# assert count_AGTC('CCT') == (0, 0, 1, 2)
# print('Проверки пройдены')
print(count_AGTC('AAAATTT'))
