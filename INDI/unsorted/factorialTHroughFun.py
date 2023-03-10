def factorTf(n):
    f = 1
    for i in range(1, n + 1):
        if n == 0:
            f=1
        else:
            f = f * i
    return f
n=int(input())
# m=factorTf(n)
print(f'Factorial {n} is {factorTf(n)}')