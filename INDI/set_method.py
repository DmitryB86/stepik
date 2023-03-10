def str_set(str):
    str_di = [i for i in str if i.isdigit()]
    set_d = sorted({e for e in str_di if str_di.count(e)>1})
    if set_d:
        print(*set_d)
    else:
        print('NO')

# str = 'abc312re542Ab'
# str_after = [s for s in str if str.count(s)<=1]
# str_after = ''.join([s for s in str if str.count(s)==1]).replace(' ','')
# print(str_after)


# ll7= []
# x = 1
# while len(ll7)<77:
#     seven = '7' * x
#     ll7.append(seven)
#     x+=1
# my_frozen = frozenset({int('7'*x) for x in range(1,78)})
# # print(len(ll7))
# print(my_frozen)