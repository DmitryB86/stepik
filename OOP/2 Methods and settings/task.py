# class Vehicle:
#     def __init__(self,max_speed,mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# # Ниже расположен код для проверок, его не нужно удалять
# modelX = Vehicle(200, 18000)
# assert modelX.max_speed == 200
# assert modelX.mileage == 18000
# assert modelX.__dict__ == {'max_speed': 200, 'mileage': 18000}
#
# audi = Vehicle(240, 5)
# assert audi.__dict__ == {'max_speed': 240, 'mileage': 5}
# print('Good')

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         return f"Hello, my name is {self.name}, and I am {self.age} years old"
#
#
# # Ниже расположен код для проверок, его не нужно удалять
# bro = Person('Nikolay', 34)
# assert bro.age == 34
# assert bro.name == 'Nikolay'
# assert bro.greet() == 'Hello, my name is Nikolay, and I am 34 years old'
#
# sister = Person('Elena', 21)
# assert sister.age == 21
# assert sister.name == 'Elena'
# assert sister.greet() == 'Hello, my name is Elena, and I am 21 years old'
# print('Good')

# Напишите определение класса Laptop
# class Laptop:
#     def __init__(self,brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.laptop_name = f'{brand} {model}'
#
# laptop1 = Laptop('hp','15-bw0xx', 57000)
# laptop2 = Laptop('lenovo', 'z-570-dx', 61000)
#
#
# assert isinstance(laptop1, Laptop)
# assert isinstance(laptop2, Laptop)
#
# hp = Laptop('hp', '15-bw0xx', 57000)
# assert hp.laptop_name == 'hp 15-bw0xx'
# assert hp.price == 57000
# assert isinstance(hp, Laptop)
#
#
# lenovo = Laptop('lenovo', 'z-570-dx', 61000)
# assert lenovo.brand == 'lenovo'
# assert lenovo.model == 'z-570-dx'
# assert lenovo.price == 61000
# assert lenovo.laptop_name == 'lenovo z-570-dx'
# assert isinstance(lenovo, Laptop)
# print('Good')

# Напишите определение класса SoccerPlayer
# class SoccerPlayer:
#     def __init__(self, name, surname, goals = 0, assists = 0):
#         self.name = name
#         self.surname = surname
#         self.goals = goals
#         self.assists = assists
#
#     def score(self,goals=1):
#         self.goals +=goals
#
#     def make_assist(self, assists = 1):
#         self.assists+=assists
#
#     def statistics(self):
#         return f'{self.surname} {self.name}- голы: {self.goals}, передачи: {self.assists}'
#
# # Ниже код для проверки методов класса SoccerPlayer
# leo = SoccerPlayer('Leo', 'Messi')
# assert isinstance(leo, SoccerPlayer)
# assert leo.__dict__ == {'name': 'Leo', 'surname': 'Messi', 'goals': 0, 'assists': 0}
# leo.score(700)
# assert leo.goals == 700
# leo.make_assist(500)
# assert leo.assists == 500
#
# leo.statistics()
#
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# assert isinstance(kokorin, SoccerPlayer)
# assert kokorin.name == 'Alex'
# assert kokorin.surname == 'Kokorin'
# assert kokorin.assists == 0
# assert kokorin.goals == 0
# kokorin.score()
# assert kokorin.goals == 1
# kokorin.score(5)
# assert kokorin.goals == 6
# kokorin.make_assist()
# assert kokorin.assists == 1
# kokorin.make_assist(10)
# assert kokorin.assists == 11
#
# kokorin.statistics()
#
#
# obi = SoccerPlayer('Оби-Ван', 'Кеноби')
# obi.make_assist()
# assert obi.name == 'Оби-Ван'
# assert obi.surname == 'Кеноби'
# assert obi.__dict__ == {'name': 'Оби-Ван', 'surname': 'Кеноби', 'goals': 0, 'assists': 1}
# obi.statistics()
#
# mila = SoccerPlayer('Mila', 'Kunis')
# mila.make_assist()
# print(mila.statistics())

class Zebra():

    def which_stripe(self):
        self.color1 = "Полоска белая"
        self.color2 = "Полоска черная"
        self.count = 0
        print(self.color1)
        self.count+=1
        if self.count%2!=0:
            print(self.color1)
            self.count+=1
        elif self.count%2==0:
            print(self.color2)
            self.count+=1


z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe()