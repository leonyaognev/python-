#x = "    Леонид    "
# print(x.strip()) #убирает символы слева и срава, указанные в скобках
# print(x.lstrip()) #убирает символы только слева
# print(x.rstrip()) #убирает символы только справа
#
# s = "+55"
# s1 = "-55"
# print(s.lstrip("+-"))
# print(s1.lstrip("+-"))
#
# s = "-=-=-=-=+_+_+_+-=-=-=55"
#
# s = s.lstrip("-+_=")
# print(s.isdigit())
#
# s = "Привет мир, я Алексей"
# print(s.split()) #разделяет по определенным знакам

# from random import randint, shuffle, choice
# print(randint(-100,100))
# arr = [1, 2, 3, 4, 5]
# shuffle(arr) #перемешать\перетусовать
# print(arr)
# print(choice(arr)) #выбрать случаянный элемент из списка

# for i in range(10):
#     if i == 5:
#         continue #пропуск итерации
#     print(i)

#пустой список
#l = []
#l = list()
#
# l = []
# l.append([1, 2, "hhfjvjnkdf", ["mkvmk", 8.4994949]])
# print(l)
#
# l1 = [1, "", True, "барабашка"]
# print(l1)
# l1.remove("барабашка") #удалить по значению
# print(l1)
# l1.pop() #удалить по индексу, () - удалить последний элемент списка
# print(l1)
# l1.pop(0)
# print(l1)
#
# l2 = (1,2,3) #кортеж - то же самое, что и список,  но неизменяемый
#
# d = {} #пустой словарь
# d = dict() #пустой словарь
#
# d = {
#     "key1": 123
#     "key2": {1: "aaaaaaaaaaaaa"}
#     True: "ss"
# # }
# #
# def aboba(x1, x2):
#     return
#
# aboba(10, 2) #вызов функции с аргументами

lambda_cube = lambda y: y*y*y

print(lambda_cube(2))