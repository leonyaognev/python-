# try:
#     x = int(input("введи число: "))
#     print(x)
# except (ValueError, IndexError):
#     print("ы")
# except TypeError:
#     print("hi")
# else:   #когда ошибок небыло
#     print("молодец что ввел число!")
# finally:    #сработает в любом случае
#     print("я сделал")
#
# x = input("как зовут воего кореша(собаку)? ")
# try:
#     if x == "лёня" or "леня":
#         raise ValueError("ты че пес")
# except ValueError:
#     print("бек-мек, пук-пук")

# задача1

# arr = 0
# a = 0
# s = open("boba.txt", "r", encoding="utf-8")
#
# x = s.read().split()
# for i in x:
#     try:
#         arr += int(i)
#     except ValueError:
#         continue
#     a += 1
#     print(a, arr)
#
# print("средне арефметическое равно: " + str(arr/a))
#
# s.close()

# задача 2

# maxi = -1
#
# try:
#     s = open("pobeditel.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("blin")
#     quit()
#
# text = s.readlines()
# s.close()
#
# for i, element in enumerate(text):
#     text[i] = element.split()
#
# print(text)
#
# for student in text:
#     try:
#       if int(student[3]) > maxi:
#           maxi = int(student[3])
#     except IndexError:
#         print("значение отсутствует", student)
#         continue
#     except ValueError:
#         print("баллы неправильно указаннаы", student)
#         continue
# print(maxi)

# задача 5

# sim = 0
# n = 0
# while True:
#     t = input("введите название файла: ")
#     try:
#         s = open(t, "r", encoding="utf-8")
#         break
#     except FileNotFoundError:
#         print("такого файла не существует(((")
#
#
# a = s.readlines()
#
# s.close()
#
#
# for i in a:
#     sim += len(i)
#
#     for b in i.split():
#         n += 1
#
# if a == []:
#     print("файл пуст :((")
# else:
#     print("слов: ", n)
#     print("символов: ", sim)
#     print("трок: ", len(a))

# задача 6

namber = 0

while True:
     t = input("введите название файла: ")
     try:
         s = open(t, "r", encoding="utf-8")
         break
     except FileNotFoundError:
         print("такого файла не существует(((")

stroka = input("введите строку, которую мы ищем: ")

file = s.read().split()

for i in file:
    if stroka == i:
        namber += 1
if namber == 0:
    print("строка в данном файле не встречается :((")
else:
    print("строка встечается ", namber, "раз")