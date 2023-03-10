# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3) key=1, value= -3
# print(d)                            # {2: [-1, -2, -3]}

def update_dictionary(d, key, value):
    d = {}
    key=int()
    value=int()
    for key in d:       # if key not in dict we should create new one
        if key not in d:
            d[key].

        d.get(key)
    # d['value']=[]  # список, который пополняется
    # for i in d[0:]:
    #     if i not in d:
    #         d['value'].append(int(i))
    #     if key not in d:
    #         d[i] = key*2


print(update_dictionary(d, 1, -1))  # None
print(d)