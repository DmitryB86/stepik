#                                   5.3 Цикл for. Обход списков и строк
# 7 из 14 шагов пройдено
# letter=input()
# sentace=input()
# lists=[]
# for i in sentace.split():
#     lists.append(i)
#
# print(lists)
# for i in lists:
#     if letter in i:
#         print(i)

#                                   Линейный поиск

# numbers=input()
# whatfind=input()
# lenn=len(numbers.split())
#
# if whatfind not in numbers:
#     print('ErrorValue')
#
# for j in range(lenn):
#     if whatfind==numbers.split()[j]:
#         print(j+1)

#На вход программе поступает список из целых чисел.
# Ваша задача найти в данном списке наименьшее положительное значение.
# В случае, если положительных значений нет, выведите строку "Empty"

# numbers=input().split()
# arrNUM=[]
# arrNUMplus=[]
# for i in numbers:
#     i=int(i)
#     arrNUM.append(i)
# for i in arrNUM:
#     if i<=0:
#         continue
#     elif i>0:
#         arrNUMplus.append(i)
# if len(arrNUMplus)>0:
#     print(min(arrNUMplus))
# else:
#     print('Empty')

# Напишите программу,
# которая находит рекордное количество вхождений (не обязательно подряд) символа в строку.

# strin=input().lower()
# maxim=[]
# for i in strin:
#     count=strin.count(i)
#     maxim.append(count)
# print(max(maxim))

                                        # Делимость на 11
# number=input()
# # number='121121'
# cetArr=[]
# necetArr=[]
# lenNum=len(number)
# for i in range(lenNum):
#     if i%2==0:
#         necetArr.append(int(number[i]))
#     else:
#         cetArr.append(int(number[i]))
# if abs(sum(cetArr)-sum(necetArr))%11==0:
#     print('YES')
# else:
#     print("NO")

                                    # 5.3 Цикл for. Обход списков и строк
                                    # 11 из 14 шагов пройдено

# s=input()
# summ=0
# lens=len(s)
# count=0
# for i in s:
#     if i.isdigit():
#         summ+=int(i)
#         count+=1
# print(count, summ)
#                                           Правильная скобочная последовательность

# print(ord(')'),ord('('))
# s=input()
# s='((()))))))))()()()))))'
open=0
closed=0
for i in s:
    if ord(i)==40:
        open+=1
    elif ord(i)==41:
        closed+=1
if open==closed:
    print('YES')
else:
    print('NO')
