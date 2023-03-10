#
# g = 'green'
# def colors(param = 'r'):
#     y = 'yellow'
#     b = 'black'
#     g = 'gray'
#
#     def colors_red():
#         r = 'red'
#         print(r)
#
#     def colors_blue():
#
#         b = 'blue'
#         print(b)
#
#     if param=='r':
#         colors_red()
#     elif param =='b':
#         colors_blue()
#     else:
#         print('i dont know')
#
# colors(param = 'b')

# def color() -> None:
#     g = 'green'
#
#     def grey() -> None:
#         nonlocal g
#         g = 'grey'
#         print(g)
#
#     grey()
#     print(g)
#
#
# color()

def calculate(x:float, y:float, operation:str='a') -> None:
    def addition(x,y):
        print(x+y)

    def subtraction(x,y):
        print(x-y)

    def division(x,y):

        print(x//y)

    def multiplication(x,y):
        print(x*y)

    if operation == 'a':
        return addition(x,y)
    elif operation == 's':
        return subtraction(x,y)
    elif operation == 'd':
        if y==0:
            print('На ноль делить нельзя!')
        else:
            return division(x,y)
    elif operation == 'm':
        return multiplication(x,y)
    else:
        print('Ошибка. Данной операции не существует')
x = int(input())
y = int(input())
st = input()
calculate(x,y,st)