# class Cat:
#     breed = 'pers'
#     def hello(*args):
#         print('Meow meow. I love fish',args)
#     def say_breed(instance):
#         print(f'my breed is {instance.breed}')
#     def say_name(instance):
#         if hasattr(instance,'name'):
#             print(f'my name is {instance.name}')
#         else:
#             print('nothing')
#     def set_value(kosh, value,age = 3):
#         kosh.name = value
#         kosh.age = age
# class Robot:
#     def say_hello(self):
#         if hasattr(self, 'name'):
#             print(f'Hello, human! My name is {self.name}')
#         else:
#             print('У робота нет имени')
#     def say_bye(self):
#         print('See u later alligator')
#     def set_name(self, value):
#         self.name = value
#
# c3po = Robot()
# r2d2 = Robot()
# r2d2.set_name('R2D@')
# c3po.say_hello()
# c3po.say_bye()
# r2d2.say_hello()
# r2d2.say_bye()
#
# Напишите определение класса Counter
# class Counter:
#     def start_from(self, value=0):
#         self.value = value
#     def increment(self):
#         self.value+=1
#     def display(self):
#         print(f'Текущее значение счетчика = {self.value}')
#
#     def reset(self):
#         self.value=0
#
# # Ниже код для проверки класса Counter
#
# c1 = Counter()
# c2 = Counter()
#
# assert isinstance(c1, Counter)
# assert isinstance(c2, Counter)
# assert c1.__dict__ == {}
# assert c2.__dict__ == {}
#
# c1.start_from(45)
# assert len(c1.__dict__) == 1
# c1.increment()
# c1.display()  # печатает 46
# c1.increment()
# c1.display()  # печатает 47
#
# c2.start_from()
# c2.display()  # печатает 0
# c2.increment()
# c2.display()  # печатает 1
#
# c1.reset()  # обнулили с1, но с2 не должен меняться
# c1.display()  # печатает 0
#
# c2.display()  # попрежнему печатает 1

# Напишите определение класса Constructor
# class Constructor:
#
#     def add_atribute(self,name,value):
#         # self.name = name
#         # self.value = value
#         setattr(self,name,value)
#
#     def display(self):
#         print(self.__dict__)
#
#
# # Ниже код для проверки класса Constructor
#
# obj1 = Constructor()
# assert obj1.__dict__ == {}
# obj1.display()
# obj1.add_atribute('color', 'red')
# assert obj1.color == 'red'
# obj1.add_atribute('width', 20)
# assert obj1.width == 20
# obj1.display()
#
# obj2 = Constructor()
# obj2.display()
# obj2.add_atribute('height', 100)
# assert obj2.height == 100
# obj2.display()
#
# obj3 = Constructor()
# obj3.display()
# obj3.add_atribute('a', 100)
# obj3.add_atribute('b', 300)
# obj3.add_atribute('c', 200)
# obj3.add_atribute('b', 1)
# assert obj3.__dict__ == {'a': 100, 'b': 1, 'c': 200}
# obj3.display()

class Point:
    def set_coordinates(self,x,y):
        # setattr(self,x,y)
        self.x = x
        self.y = y

    def get_distance(self,obj):
        if isinstance(obj, Point):
            return ((self.x - obj.x)**2+(self.y-obj.y)**2)**0.5
        else:
            print('Передана не точка')
# Код ниже не удаляйте, он нужен для проверок
p1 = Point()
p2 = Point()
assert isinstance(p1, Point)
assert isinstance(p2, Point)

p1.set_coordinates(1, 2)
assert p1.x == 1
assert p1.y == 2
p2.set_coordinates(4, 6)
assert p2.x == 4
assert p2.y == 6
assert p1.get_distance(p2) == 5.0
p3 = Point()
p3.set_coordinates(10, 10)
p1.set_coordinates(4, 2)
assert p1.get_distance(p3) == 10.0
res = p1.get_distance(10)  # Распечатает "Передана не точка", вернет None
assert res is None, 'Метод get_distance должен возвращать None, если в него была передана не точка'

assert p2.get_distance([1, 2, 3]) is None  # Распечатает "Передана не точка", вернет None