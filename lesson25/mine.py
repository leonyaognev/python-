# class Class:
#     pkz = True # статический публичный атибут
#     __pkz2 = True # статический приватый атибут
#     def __init__(self, x="слово"): #значение по умолчанию
#         self.pkz1 = x # сатический публичный атрибут
#         self.pkz3 = x  # сатический приватный атрибут
#
# obg = Class()
# print(obg.pkz)
# print(obg.pkz1)
from human import Human
from house import House
from Tk import *

chel = Human("джоджо",10000)
small = House("далеко", 1_000_000_000)
normal = House("ну типа рядом", 5_000_000_000)
big = House("вот прям очень близко", 10_000_000_000)


# chel.buy_house(small, small.final_prise(0))
# print(chel.dom)
# try:
#     print(small.owner)
# except AttributeError:
#     print('хозяина нет')
#
# chel.earn_money()
# chel.earn_money()
# chel.earn_money()
# chel.earn_money()
#
# chel.buy_house(small, small.final_prise(0))
# print(chel.dom)
#
# try:
#     print('мой хозяин:', small.owner)
# except AttributeError:
#     print('хозяина нет')

