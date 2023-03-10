# import math
#
# list_g = [x**2 for x in range(1,10)]
# print(list_g)
#
# list_gen = (math.sqrt(x) for x in range(1,10))
# print(tuple(list_gen))

# from_10_to_20 = (x for x in range(10,21))
# print(next(from_10_to_20))
# print(next(from_10_to_20))
# print(next(from_10_to_20))
#
# for value in from_10_to_20:
#     print(value)

# words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon', 'drop', 'produce', 'acquisition',
#          'cheap', 'strength', 'master', 'perception', 'noise', 'strange', 'am']
#
# lens = (len(x) for x in words)
#
# for i in lens:
#     print(i)

# def facr(n):
#     pr=1
#     for i in range(1, n+1):
#         pr=pr*i
#         yield pr
#
# s = facr(11234)
# for i in facr(2342342):
#     print(i)

# def gen_squares(n):
#     for i in range(1, n+1):
#         yield i**2
#
# for i in gen_squares(5):
#     print(i)

    def gen_fibonacci_numbers(n):
        a,b = 1,1
        for __ in range(n):
            yield a
            a,b = b,a+b



for i in gen_fibonacci_numbers(10):
    print(i)

