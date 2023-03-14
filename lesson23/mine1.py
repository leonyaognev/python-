# class Person:     # объявление класса
#     def __init__(self, imya, vozrast):  # метод инициализации
#         self.age = vozrast  # Установка значений атрибутов
#         self.name = imya
#     def __str__(self):
#         return  'бархатные тяги'
#     def __getitem__(self, item):
#         print('Подкрадули кротячьи', item)
#
# leha = Person("леха", -32)
#
# print(leha)
# print(leha.age)
# print(leha.name)
# class Kefteme:
#
#
# obj = Kefteme()
# obj[2]
# class Person:
#     def __init__(self, age, name, familiya):
#         self.age = age
#         self.name = name
#         self.surname = familiya
#     def __str__(self):
#         return (f'я {self.name, self.surname}, мне {self.age}')
#     def geet(self):
#         return (f'я {self.name, self.surname}, мне {self.age}')
#
#
# chel = Person(13, "petya", "vasechkin")
#
# print(chel)
# import random
# class Person:
#     def __init__(self, age, name, familiya, ozen):
#         self.age = age
#         self.name = name
#         self.surname = familiya
#         self.ozen = ozen
#         self.sr = sum(ozen) / len(ozen)
#     def __str__(self):
#         return (f'я {self.name} {self.surname}, мне {self.age}')
#
# chel1 = (Person(13, "petya", "vasechkin", [random.randint(2, 5) for i in range(random.randint(10, 50))]))
# chel2 = (Person(13, "коля", "васечкин", [random.randint(2, 5) for i in range(random.randint(10, 50))]))
# chel3 = (Person(13, "гриша", "васечкин", [random.randint(2, 5) for i in range(random.randint(10, 50))]))
# chel4 = (Person(13, "гоша", "васечкин", [random.randint(2, 5) for i in range(random.randint(10, 50))]))
# chel5 = (Person(13, "даша", "васечкина", [random.randint(2, 5) for i in range(random.randint(10, 50))]))
#
# students = [chel1, chel2, chel3, chel4, chel5]
#
# # d = {
# #     chel1: chel1.ozen,
# #     chel2: chel2.ozen,
# #     chel3: chel3.ozen,
# #     chel4: chel4.ozen,
# #     chel5: chel5.ozen
# # }
# d = {}
#
# for i in students:
#     d[i.name] = i.sr
#
# d1 = {}
# for i in reversed(sorted(d.values())):
#     for key in d.keys():
#         if d[key] == i:
#             d1[key] = d[key]
#             break
# print(d1)
# # задача 3
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"{self.x}, {self.y}"
#
#
# class Rectangle:
#     def __init__(self, point1, point2):
#         self.point1 = point1
#         self.point2 = point2
#     def  __str__(self):
#         return f"{self.point1}, {self.point2}"
#
# pt1 = Point(123, 15)
# pt2 = Point(858, 636)
# kvadrat = Rectangle(pt1, pt2)
# ptx1 = int(str(kvadrat.point1).split(',')[0])
# ptx2 = int(str(kvadrat.point1).split(',')[1])
# pty1 = int(str(kvadrat.point2).split(',')[0])
# pty2 = int(str(kvadrat.point2).split(',')[1])
# print(ptx1, ptx2, pty1,pty2)
# osx = ptx2 - ptx1
# osy = pty2 - pty1
# print(osy*osx)
# задача 4
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"{self.x}, {self.y}"
#
#
# class Rectangle:
#     def __init__(self, point1, point2):
#         self.point1 = point1
#         self.point2 = point2
#     def has_point(self, tochka):
#         self.point = tochka
#         if (self.point1.x <= self.point.x <= self.point2.x) and (self.point1.y <= self.point.y <= self.point2.y):
#             print(True)
#         else:
#             print(False)
#
#     def  __str__(self):
#         return f"{self.point1}, {self.point2}"
#
#
#
# pt1 = Point(123, 15)
# pt2 = Point(858, 636)
# pt3 = Point(122, 100)
# kvadrat = Rectangle(pt1, pt2)
# toch = kvadrat.has_point(pt3)
# задача
# import random
# class Wall:
#     def __init__(self, x):
#         self.x = x
#         self.y = random.randint(1,10)
#     def print_figure(self):
#         for i in range(self.y):
#             a = '  _'
#             b = '|_|'
#             print(a * self.x,'\n', b * self.x)
#
#
# obj = Wall(5)
# obj.print_figure()
# import random
# class Wall:
#     def __init__(self, x):
#         self.x = x
#         self.y = random.randint(1,10)
#     def print_figure(self):
#         for i in range(self.y):
#             a = '  _'
#             b = '|_|'
#             print(a * self.x,'\n', b * self.x)
#
#
# obj.print_figure()
# obj = Wall(5)
# ==========================================
class Coffe:
    def __init__(self, money, milk, water, coffe):
        self.money = money
        self.milk = milk
        self.water = water
        self.coffe = coffe
    def __str__(self):
        return (f'деньги: {self.money}\nмолоко: {self.milk}\nвода: {self.water}\nкоффе: {self.coffe}')
    def latte(self):
        self.money, self.milk, self.water, self.coffe = self.money - 50, self.milk - 150, self.water - 200, self.coffe - 24
    def espresso(self):
        self.money, self.milk, self.water, self.coffe = self.money - 35, self.milk - 0, self.whoter - 50, self.coffe - 18
    def cappuccino(self):
        self.money, self.milk, self.water, self.coffe = self.money - 45, self.milk - 0, self.whoter - 250, self.coffe - 24

auto = Coffe(70, 200, 400, 60)
while True:
    user = int(input('''какой вы хотите кофе?
        1)латте
        2)еспрессо
        3)капучино
ввод: '''))

    if user == 1:
        auto.latte()
        if input(f'Пожалуйста внесите оплату в размере {auto.latte.lprise()}руб.\n оплата(руб): ') == 42:
            print('lf ')
    elif user == 2:
        auto.espresso()
    elif user == 3:
        auto.cappuccino()
        print(auto)
    elif user == "отчет " or user == "отчет":
        print(auto)
    else:
        print('ыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыы')








