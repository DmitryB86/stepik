def sum_num(n):
    s=0
    for i in n:
        if i.isdigit():
            s=s+int(i)
    print(s)

n=input()
sum_num(n)