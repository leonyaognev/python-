import json
#
# f = open("data.json", "w", encoding="utf-8")
#
# salad = {
#     "Tomato": [5, "Cut"],
#     "Cucumber": [3, "Сheck cucumbers for bitterness", "Cut"],
#     "Salt": "add to taste",
#     "Sugar": False
# }
# json.dump(salad, f, ensure_ascii=False) # dump записывает файл
# json.dumps(salad)
# print(json.dumps(salad)) #перевод в данные json
#
# f.close
#
# f = open("data.json", "r")
#
# content = json.load(f)
#
# f.close()
# print(content)
#
# f = open("biblia.txt", "r", encoding="utf-8")
#
# x = f.readlines()
# f.close()
#
# slov = {}
# for i in x:
#     k = i.split(": ")
#     slov[k[0]] =  k[1].rstrip()
#
# print(slov)
#
# f = open("data.json", "w", encoding="utf-8")
#
# json.dump(slov, f, ensure_ascii=False)
#
# f.close()
#
# f = open("data.json", "r", encoding="utf-8")
#
# content = json.load(f)
#
# f.close()
#
#
# for i, element in enumerate(content):
#     a = type(element)
#     print(i,element)
#     if a == str:
#         content[i] = element + "!"
#     elif a == int or a == float:
#         content[i] = element + 1
#     elif a == bool:
#         content[i] = not content[i]
#     # elif a == None:
#     #     del content[i]
#     elif a == list:
#         content[i] += content[i]
#     elif a == dict:
#         content[i] = element[i]["newkey"] = None
#     print(a, content)
# import requests
# resp = requests.get("http://api.open-notify.org/iss-now.json", )
# data = resp.json()['iss_position']
# print(f"долгота: {data['longitude']}, широта:{data['latitude']}")

import requests

sun = requests.get('https://api.sunrisesunset.io/json?lat=55.0415&lng=82.9346&timezone=UTC&date=today').json()
print(sun)
sunset = sun['results']['last_light']
sunrise = sun['results']['first_light']
sunset = sunset.split(' ')
sunrise = sunrise.split(' ')
timeset = sunset[0].split(':')
timerise = sunset[0].split(':')
print(timeset,timerise)
print(sunrise, sunset)
time



