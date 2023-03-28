# class Point:
#     def __init__(self, coord_x = 0,coord_y = 0 ):
#         self.move_to(coord_x,coord_y)
#
#     def move_to(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#     def go_home(self):
#         self.move_to(0,0)
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width*self.height
#     def perimeter(self):
#         return 2*(self.width+self.height)
#
#
# r1 = Rectangle(2,3)
# print(r1.width)

# Напишите определение класса Stack
class Stack:

    # values = []

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if Stack.is_empty:
            print('Empty Stack')
        del_i = self.values.pop(self.values.index(Stack.peek(self)))
        return del_i

    def peek(self):
        if Stack.is_empty:
            print('Empty Stack')
            return None
        return self.values[-1]

    def is_empty(self):
        if Stack.size(self)==0:
            return True
        return False

    def size(self):
        return len(self.values)

# Ниже код для проверки класса Stack

# s = Stack()
# # print(s.values)
# # print(isinstance(s, Stack))
#
# s.peek()
# print(s.is_empty())
# s.push('cat')
# print(s.size())
# print(s.peek())
#
# s.push('dog')
# print(s.size())
# print(s.peek())
#
#
# s.push(True)
# print(s.size())
# print(s.is_empty())
# print(s.values)
# s.push(777)
# # assert s.size() == 4
# #
# print(s.pop())
# print(s.size())
#
# assert s.pop() is True
# assert s.size() == 2
#
# s.push(123)
# s.push(123456)
# assert s.peek() == 123456
# assert s.size() == 4
#
# assert s.pop() == 123456
# assert s.pop() == 123
# assert s.pop() == 'dog'
# assert s.is_empty() is False
# assert s.pop() == 'cat'
# assert s.is_empty() is True
#
d = Stack()
assert d.peek() is None  # Печатает "Empty Stack"
assert d.pop() is None  # Печатает "Empty Stack"
d.push('hello')
assert d.size() == 1
d.push('world')
assert d.size() == 2
assert d.peek() == 'world'
assert d.pop() == 'world'
assert d.peek() == 'hello'