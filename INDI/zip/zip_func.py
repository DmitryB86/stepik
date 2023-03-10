



# count_strings(1, 2, 'hello', [2, 3, 4], True) => 1
# count_strings('am', 'world', 'hello', 'is') => 4
# count_strings() => 0
# count_strings(True, False) => 0
#

# def count_strings(*args):
#     s_sum = 0
#     for i in args:
#         if isinstance(i,str):
#             s_sum+=1
#
#     return s_sum
#
#
# print(count_strings(1, 2, 'hello', [2, 3, 4], True))

# find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]) => ['A', 'b', 't', 'W']
#
# find_keys(name='Bruce', surname='Wayne') => []
#
# find_keys(marks=[4, 5], name='ashle', surname='Brown', age=20, Also=(1, 2)) => ['Also', 'marks']

# def find_keys(**kwargs):
#     rez_list = []
#     for k,v in kwargs.items():
#         if isinstance(v, (tuple,list)):
#             rez_list.append(k)
#     return sorted(rez_list, key= lambda x:x.lower())
#
#
# print(find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]))

import pycountry
from pprint import pprint
z = list(pycountry.countries)
print(z[4])

