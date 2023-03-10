import json

with open('manager_sales.json', 'r') as f:
    data  = json.load(f)
dict_sales = {}
for element in data:
    summ = 0
    # print(element['manager']['first_name'])
    full_name = element['manager']['first_name']+' '+element['manager']['last_name']
    for cars in element['cars']:
        summ+=cars['price']
    dict_sales[full_name]=summ

v=list(dict_sales.values())
k=list(dict_sales.keys())
print(k[v.index(max(v))], max(v))