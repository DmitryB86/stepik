#
# def header(func):
#
#     def inner(*args, **kwargs):
#         print('<header>')
#         func(*args, **kwargs)
#         print('</header>')
#     return inner
#
# def table(func):
#
#     def inner(*args, **kwargs):
#         print('<table>')
#         func(*args, **kwargs)
#         print('</table>')
#     return inner
#
# def text_decor(func):
#     def inner(*args, **kwargs):
#         print('Hello')
#         func(*args,**kwargs)
#         print('Goodbye!')
#     return inner
#
# @header # say = header(say)
# def say(name,sername):
#     print(f'hello {name} {sername}')

# # def buy():
# #     print('buy buy wwww')
#
# # say = table(header(say))
# say('INNA', 'Petrova')
# # buy = decorator(buy)
# # buy()
def double_it(func):

    def inner(*args,**kwargs):
        return func(*args,**kwargs)*2

    return inner
#
# @double_it
# def get_sum(*args):
#     return 2*sum(args)

@double_it
def multiply(num1, num2):
    return num1 * num2

res = multiply(9, 4) # произведение 9*4=36, но декоратор double_it удваивает это значение
print(res)
#
# res = get_sum(1, 2, 3, 4, 5)
# print(res) # печатает 30