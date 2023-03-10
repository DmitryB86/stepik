# goods = dict()
# while True:
#     st = input()
#     if st != 'конец':
#         goods[st.split(':')[0]]=st.split(':')[1]
#     else:
#         break
# for v,k in sorted(goods.items(), key= lambda item: item[1],reverse=True):
#     print(v)

goods = dict()
while True:
    st = input()
    if st != 'конец':
        # {x: x ** 2 + 1 for x in range(5)}
        # goods = {st.split(':')[0]:st.split(':')[1] for st in input() }
        goods[st.split(':')[0]]=st.split(':')[1]
    else:
        break
for v,k in sorted(goods.items(), key= lambda item: item[1],reverse=True):
    print(v,k)