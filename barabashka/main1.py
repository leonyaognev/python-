# ass = ['A', 'b', 'c', 'd']
# #
# # for i in ass:
# #     print(i)
# #
# # for i in range(len(ass)):
# #     print(i)
# #
# for indx, elem in enumerate(ass):
#     print(indx, elem)
# словари
# d = {}
# d1 = dict()
#
# d['Key'] = "znak" #добавляет значение в словарь
# d['Key1'] = "val1" #добавляет значение в словарь
# d['Key2'] = "val2" #добавляет значение в словарь
# del d['Key1']
# print(d)
#
# # for i in d.values(): #перебор значений
# #     print(i)
# #
# # for i in d: #перебор ключей
# #     print(i)
# d = {1: 'o', 2: 'b'}
# # l_keys = list(d.keys())
# # print(l_keys)
# # l_val = list(d.values())
# # print(l_val)
# for i in d.items():
#     print(i)
#множества
# s = set() #пустое множество
#
# l = [1, 2, 3, 4, 5, 4, 4, 3, 7, 0]
#
# s = set(s)
# if len(s) != len(l):
#     print(True) # дубликаты есть
# else:
#     print(False) # дубликатов нет
#
# s1 = {1, 2, 3, 4, 5}
# s2 = {3, 4, 5, 6, 7}
# print(s1.union(s2)) # можно, но не удобно (объеденение)
# print(s1 | s2) # просто, удобно и без заморочек
# print(s1 - s2) # разность .differnce
# print(s1 & s2) #  пересечение .intersection
# print(s1 ^ s2) # ассиметрическая разность .
l = [i ** 2 for i in range(1, 6)] #list comprehension
print(l)
            