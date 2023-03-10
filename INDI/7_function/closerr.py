


# def main_f(name):
#
#     def inner_f():
#
#         print('hello baby', name)
#     return inner_f
#
# def adder(value):
#     def inner(a):
#         return value+a
#     return inner

# def counter():
#     count = 0
#     def inner():
#         nonlocal count
#         count+=1
#         return count
#     return inner


# def multiply(value):
#
#     def inner(a):
#         return f"Умножение {value} на {a} = {value*a}"
#     return inner

# def avarage_num():
#     numbers = []
#     def inner(num:int):
#         numbers.append(num)
#         print(numbers)
#         return sum(numbers)/len(numbers)
#     return inner

# from datetime import datetime


def names():
    name_list=[]
    def inner(name):
        name_list.append(name)
        return name_list
    return inner
def counter():
    count = 0
    def inner(value):
        nonlocal count
        count+=value
        return count
    return inner

count = counter()
print(count(2))
print(count(6))
print(count(7))
print(count(-10))



boys = names()
girls = names()
print(boys('Ivan'))
print(boys('Alex'))
print(boys('Oleg'))
print(girls('Alena'))
print(girls('Veronika'))
print(girls('Irina'))