# class FiftyFifty:
#     def __init__(self):
#         self.money = 0.05
#         self.__zarplata = 20_000
#     def ipotek(self): #public метод
#         if self.__zarplata > 75_000: #ИСПОЛЬЗОВАНИЕ ПРИВАТНЫХ ДАННЫХ
#             return True
#         else:
#             return False
#     def povishenie(self): #public метод
#         self.__zarplata += 30_000
#     def __bar (self): #private метод
#         return True
#     def gou(self):
#         if self.__zarplata > 1:
#             print(self.__bar)
#
# sanya = FiftyFifty()
# # print(sanya.money)
# # sanya.__zarplata = 21_000 #public
# # sanya._FiftyFifty__zarplata = 21_000 #privat
# # print(sanya.ipotek())
# # sanya.povishenie()
# # print(sanya.ipotek())
# # sanya.povishenie()
# # print(sanya.ipotek())
#
# print(sanya.gou())

# задача1

# class Car:
#     def __init__(self):
#         self.__on = 0
#     def color(self, x):
#         self.color = x
#         return self.color
#     def type(self, x):
#         self.type = x
#         return self.type
#     def year(self, x):
#         self.year = x
#         return self.year
#     def on(self):
#         if self.__on == 0:
#             self.__on = 1
#             return 'машна заведена'
#         else:
#             return 'ты дачек?'
#     def off(self):
#         if self.__on == 1:
#             self.__on = 0
#             return 'сдох'
#         else:
#             return 'ты дачек?'
#
# mashina = Car()
# print(mashina.color('перпл'))
# print(mashina.type('легкоушечка'))
# print(mashina.year('ранний полеозой'))
# print(mashina.on())
# print(mashina.on())
# print(mashina.off())
# print(mashina.off())

#=========================
# import string
# string.ascii_lowercase
# class Alphabet:
#     def __init__(self):
#         self.__lang = 'eng'
#         self.__letters = string.ascii_lowercase
#     def print(self):
#         return self.__letters
#     def letters_num(self):
#         return len(self.__letters)
#
# A = Alphabet()
# print(A.print())
# print(A.letters_num())

#=================

# import datetime
# class Time:
#     def __init__(self):
#         self.time = datetime.datetime.now().time().strftime('%H:%M:%S')
#         self.time = self.time.split(':')
#         self.hour, self.min, self.sec = int(self.time[0]), int(self.time[1]), int(self.time[2])
#     def __h(self):
#         if self.hour >= 24:
#             self.hour = 0
#     def __m(self):
#         if self.min >= 60:
#             self.min
#     def hplus(self):
#         self.hour += 1
#     def mplus(self):
#         self.min += 1
#     def splus(self):
#         self.sec += 1
#     def coc(self):
#         return str(self.hour).rjust(2, '0') + ':' + str(self.min).rjust(2, '0') + ':' + str(self.sec).rjust(2, '0')
#
# time = Time()

#========================
from random import choice

class Blablabla:
    def __init__(self):
        self.__couner = 5
    def increment(self):
        self.__couner += 1
    def decrement(self):
        self.__couner -= 1
    def ret(self):
        return self.__couner

counter = Blablabla()
l = [counter.increment, counter.decrement]

while 0 < counter.ret() < 10:
    choice(l)()
    print(counter.ret())
