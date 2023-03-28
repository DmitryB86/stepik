# class Cat:
#
#
#     def __init__(self,name,age=2, breed='rus blue', color = 'grey'):
#         print('My name is obj:',self)
#         self.name = name
#         self.age = age
#         self.breed = breed
#         self.color = color

# class Car:
#     def __init__(self, model='opel', color='black', engine=0, s_power=0, doors=0):
#         self.model = model
#         self.color = color
#         self.engine = engine
#         self.power = s_power
#         self.doors = doors
#
# bmw = Car('bmw','grey',1200,4,4)
# print(bmw.__dict__)
# new_car = Car(engine=3,s_power=12,doors=2)
# print(new_car.__dict__)
class Zebra:
    def __init__(self):
        self.white = 'Полоска белая'
        self.black = 'Полоска черная'

    def which_stripe(self):
        print(self.white)
        self.white,self.black=self.black,self.white

z1 = Zebra()
print(z1.which_stripe())
print(z1.which_stripe())
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe()