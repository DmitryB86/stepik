def count_letters(stringg):
    # str = input()
    N,K=0,0
    for i in stringg:
        if i.isupper():
            N+=1
        elif i.islower():
            K+=1
        else:
            continue
    print(f'Количество заглавных символов: {N}')
    print(f'Количество строчных символов: {K}')

str=input()
count_letters(str)