
# # # # n=int(input())
# # # n=5
# # # ddic={i**2 for i in range(1,n+1)}
# # # # for i in range(1,n+1):
# # # #     ddic[i] = i**2
# # #
# # # print(ddic)
# #
# # from string import ascii_lowercase
# #
# #
# # ddic={}
# # st= ascii_lowercase
# # st = st.split()
# # print(st)
# # # j=1
# # # for i in ascii_lowercase:
# # #     ddic[i]=j
# # #     j+=1
# # # print(ddic)\
# # account = {
# #   "id": 5681,
# #   "uid": "45f17b56-bcad-4933-8c73-a37aaa6863b9",
# #   "account_number": "6733198878",
# #   "iban": "GB79PNXF20678598570754",
# #   "bank_name": "AAC CAPITAL PARTNERS LIMITED",
# #   "routing_number": "007398728",
# #   "swift_bic": "AACCGB21"
# # }
# # print(len(account))
# currencies = {
#     'Argentine Peso': 118362.205708,
#     'Australian Dollar': 1586.232315,
#     'Bahraini Dinar': 423.780164,
#     'Botswana Pula': 13168.450636,
#     'Brazilian Real': 5954.781483,
#     'British Pound': 834.954104,
#     'Bruneian Dollar': 1520.451015,
#     'Bulgarian Lev': 1955.83,
#     'Canadian Dollar': 1430.54405,
#     'Chilean Peso': 898463.818465,
#     'Chinese Yuan Renminbi': 7171.445692,
#     'Colombian Peso': 4447741.922165,
#     'Croatian Kuna': 7527.744707,
#     'Czech Koruna': 24313.797041,
#     'Danish Krone': 7440.613895,
#     'Emirati Dirham': 4139.182587,
#     'Hong Kong Dollar': 8786.255952,
#     'Hungarian Forint': 355958.035747,
#     'Icelandic Krona': 143603.932438,
#     'Indian Rupee': 84241.767127,
#     'Indonesian Rupiah': 16187150.010697,
#     'Iranian Rial': 47534006.535121,
#     'Israeli Shekel': 3569.191411,
#     'Japanese Yen': 129149.364679,
#     'Kazakhstani Tenge': 489292.515538,
#     'Kuwaiti Dinar': 340.959682,
#     'Libyan Dinar': 5196.539901,
#     'Malaysian Ringgit': 4717.485104,
#     'Mauritian Rupee': 49212.933037,
#     'Mexican Peso': 23130.471272,
#     'Nepalese Rupee': 134850.008728,
#     'New Zealand Dollar': 1703.649473,
#     'Norwegian Krone': 9953.078431,
#     'Omani Rial': 433.360301,
#     'Pakistani Rupee': 198900.635421,
#     'Philippine Peso': 57574.278782,
#     'Polish Zloty': 4579.273862,
#     'Qatari Riyal': 4102.552652,
#     'Romanian New Leu': 4946.638369,
#     'Russian Ruble': 86197.012666,
#     'Saudi Arabian Riyal': 4226.530892,
#     'Singapore Dollar': 1520.451015,
#     'South African Rand': 17159.831129,
#     'South Korean Won': 1355490.097163,
#     'Sri Lankan Rupee': 228245.645722,
#     'Swedish Krona': 10439.125427,
#     'Swiss Franc': 1037.792217,
#     'Taiwan New Dollar': 31334.286611,
#     'Thai Baht': 37436.518169,
#     'Trinidadian Dollar': 7636.35428,
#     'Turkish Lira': 15078.75981,
#     'US Dollar': 1127.074905,
#     'Venezuelan Bolivar': 511082584.868731
# }
# st = input()
# if st in currencies:
#     print(currencies[st])
# else:
#     print(f'Нет данных по {st}')
# account = {
#   "id": 3136,
#   "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
#   "account_number": "0847799459",
#   "iban": "GB90XTND56373623909314",
#   "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
#   "routing_number": "126602476",
#   "swift_bic": "BCYPGB2LHGB"
# }
#
# keys = list(i for i in account)
# print(keys)

# d1 = {'a': 100, 'b': 200, 'c': 333}
# d2 = {'x': 300, 'y': 200, 'z': 777}
#
# d1.update(d2)
# print(d1)
#
# n=int(input())
# names={}
# for i in range(n):
#     st=input()
#     if st in names:
#         print(f'{st}{names[st]}')
#         names[st]+=1
#     else:
#         print('OK')
#         names[st]=1


#
# countries = {
#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],
#     "Norway": ["Oslo", "Bergen", "Trondheim"],
#     "England": ["London", "Birmingham", "Manchester"],
#     "Germany": ["Berlin", "Hamburg", "Munich"],
#     "France": ["Paris", "Marseille", "Toulouse"]
# }
#
# city = input()
# # city='London'
#
# count=[]
# for key in countries:
#     if city in countries[key]:
#         count.append(key)
#
#
# if len(count)>=1:
#     print(f'INFO: {city} is a city in {count[0]}')
# else:
#     print(f'ERROR: Country for {city} not found')
#     #

# workers = {
#     'employer1': {'name': 'Jhon', 'salary': 7500},
#     'employer2': {'name': 'Emma', 'salary': 8000},
#     'employer3': {'name': 'Brad', 'salary': 500}
# }
# workers['employer3']['salary']=8500
# print(workers)

# dict={}
# # st=input()
# st='aassdjfJDKF9385FFFHlkds028(*$@'
# for i in st.lower():
#     if i.isalpha():
#        dict[i]=dict.get(i,0) +1
#         # if i in dict:
#         #     dict[i]+=1
#         # else:
#         #     dict[i]=1
# print(dict)

# supermarket = {
#     "milk": {"quantity": 20, "price": 1.19},
#     "biscuits": {"quantity": 32, "price": 1.45},
#     "butter": {"quantity": 20, "price": 2.29},
#     "cheese": {"quantity": 15, "price": 1.90},
#     "bread": {"quantity": 15, "price": 2.59},
#     "cookies": {"quantity": 20, "price": 4.99},
#     "yogurt": {"quantity": 18, "price": 3.65},
#     "apples": {"quantity": 35, "price": 3.15},
#     "oranges": {"quantity": 40, "price": 0.99},
#     "bananas": {"quantity": 23, "price": 1.29}
# }
#
# summ=0
# for value in supermarket.values():
#     summ+=(value['price']*value['quantity'])
#
# print(summ)

# s1 = 'abracadabra'
# s1_dic={}
# s2 = 'cadabaabra'
# s2_dic={}
# for i in s1:
#     s1_dic[i]=s1_dic.get(i,0)+1
# for j in s2:
#     s1_dic[j]=s1_dic.get(j,0)+1
# if sorted(s1)==sorted(s2):
#     print('YES')
# else:
#     print('NO')
# persons= [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
# data={}
# for i in persons:
#     sub_data={}
#     sub_data["salary"]=i[1]
#     sub_data["gender"]=i[2]
#     sub_data["passport"]=i[3]
#     if i not in data:
#         data[i[0]] = sub_data
#         # print(i[1], type(i))
# for i in data:
#     print(i, data[i])

# data = {'my_friends': {'count': 10,
#                        'people': [{'bdate': '31.8.2005',
#                                    'first_name': 'Kurt',
#                                    'id': 621547005,
#                                    'last_name': 'Cobain'},
#                                   {'first_name': 'Виолетта',
#                                    'id': 484200150,
#                                    'last_name': 'Кастилио'},
#                                   {'bdate': '28.8.1942',
#                                    'first_name': 'Иринка',
#                                    'id': 21886133,
#                                    'last_name': 'Бушуева'},
#                                   {'bdate': '4.7.2002',
#                                    'first_name': 'Данил',
#                                    'id': 282456573,
#                                    'last_name': 'Греков'},
#                                   {'bdate': '25.5',
#                                    'first_name': 'Валентин',
#                                    'id': 184902932,
#                                    'last_name': 'Долматов'},
#                                   {'bdate': '6.12.1982',
#                                    'first_name': 'Евгений',
#                                    'id': 620469646,
#                                    'last_name': 'Шапорин'},
#                                   {'bdate': '4.11.1995',
#                                    'first_name': 'Ангелина',
#                                    'id': 622328862,
#                                    'last_name': 'Краснова'},
#                                   {'bdate': '2.2.1915',
#                                    'first_name': 'Иван',
#                                    'id': 576015198,
#                                    'last_name': 'Вирин'},
#                                   {'bdate': '27.9',
#                                    'first_name': 'Паша',
#                                    'id': 386922406,
#                                    'last_name': 'Воронов'},
#                                   {'bdate': '20.12',
#                                    'first_name': 'Ольга',
#                                    'id': 622170942,
#                                    'last_name': 'Савченкова'}]
#                        }
#         }
# dict_final=[]
# for i in data['my_friends']["people"]:
#     dict_final.append(i['first_name'])
#
# for i in sorted(dict_final):
#     print(i)

# dicc={f'Квадрат числа {i}':i**2 for i in range(1,11)}
# print(dicc)

# user = {
#     "id": 4170,
#     "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
#     "password": "SyUpfo1ljm",
#     "first_name": "Teresa",
#     "last_name": "Wehner",
#     "username": "teresa.wehner",
#     "email": "teresa.wehner@email.com",
#     "gender": "Non-binary",
#     "phone_number": "+674 424.561.2776",
#     "social_insurance_number": "637316241",
#     "date_of_birth": "1993-08-17",
#     "employment": {
#         "title": "Central Hospitality Liaison",
#         "key_skill": "Organisation"
#     },
#     "subscription": {
#         "plan": "Essential",
#         "status": "Idle",
#         "payment_method": "Debit card",
#         "term": "Annual"
#     }
# }
#
# # st=input().split()
# st='uid last_name password'
# # new_dic={}
# # for i in st.split():
# #     for key, value in user.items():
# #         if i == key:
# #             new_dic[key]=value
# # print(new_dic)
#
# new_dic={key:user[key] for key in input().split()}
#
# print(new_dic)

people = [
    ['Amy Smith', '694.322.8133x22426'],
    ['Brian Shaw', '593.662.5217x338'],
    ['Christian Sharp', '118.197.8810'],
    ['Sean Schmidt', '9722527521'],
    ['Thomas Long', '163.814.9938'],
    ['Joshua Willis', '+1-978-530-6971x601'],
    ['Ann Hoffman', '434.104.4302'],
    ['John Leonard', '(956)182-8435'],
    ['Daniel Ross', '870-365-8303x416'],
    ['Jacqueline Moon', '+1-757-865-4488x652'],
    ['Gregory Baker', '705-576-1122'],
    ['Michael Spencer', '(922)816-0599x7007'],
    ['Austin Vazquez', '399-813-8599'],
    ['Chad Delgado', '979.908.8506x886'],
    ['Jonathan Gilbert', '9577853541']
]

phone_book={person[1]:person[0] for person in people}

# print(people[2])
print(phone_book)