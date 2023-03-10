def factorial(x):
    f=1
    i=1
    while i!= x+1:
        f=f*i
        i+=1
    return f
n=int(input())
k=int(input())
c=factorial(n)/(factorial(k)*factorial(abs(n-k)))
print(c)

# f=1
# i=1
# while i!=n+1:
#     f=f*i
#     i+=1
# print(f)