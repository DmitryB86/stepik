import json
from pprint import pprint
from random import randint
from datetime import datetime
# str_json = """
# {
#     "response": {
#         "count": 5961878,
#         "items": [{
#
#             "first_name": "Елизавета",
#             "id": 620471795,
#             "last_name": "Сопова",
#             "can_access_closed": true
#                 },
#                 {
#             "first_name": "Роман",
#             "id": 614752515,
#             "last_name": "Малышев",
#             "can_access_closed": true
#                 }]
#                 }
# }"""

# print(type(str_json))

# data = json.loads(str_json)
# pprint(type(data))
# for item in data['response']['items']:
#     del item['id']
#     item['likes'] = randint(1,20)
#     item['ttype'] = None
#     item['time'] = datetime.now().strftime('%m')

# print(data['response']['items'])

# with open('my.json','r') as f:
#     data = json.load(f)
# print(data)
# # new_json = json.dumps(data, indent=2)
# # # print(new_json)
# # print(json.loads(new_json))

dict_j ={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

json_data = json.dumps(dict_j)
print(json_data)
