
# lambda arg,arg2...: executing

# r = lambda x: x*x*x
# ssum = lambda a,b,c: a+b+c
# per = lambda e,y,o: ssum(e,y,o)
# sds = lambda x: x**2 if x>5 else x**4
#
# print(r(2))
# print(per(10,12,33))
# print(sds(6))
# def f(x):
#     return x%10
#
# sp = [12,343,451,54330,66,747,898]
# sp.sort(key=lambda x: x%10)
# print(sp)

# adding_10 = lambda x: x+10
# print(adding_10(34))

# starts_with = lambda st: True if st[0]=='W' else False
# sale_lambda = lambda x: x*0.9
# sq = lambda x, y: x**2 + y**2

average = lambda *args: sum(list(args))/len(list(args))
print(average(4,4,5))

