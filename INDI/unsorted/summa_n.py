def summ_n(t):
    s=0
    for i in range(1,t+1):
        s=s+i
    print(f'Я знаю, что сумма чисел от 1 до {t} равна {s}')
t=int(input())
summ_n(t)


