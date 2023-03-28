from Person import Person
import random


def ofor():
    u = random.choice(users)
    print(f'логин: {u.login}')
    print(f'имя: {u.name}')
    print(f'фамилия: {u.surname}')
    print(f'посты: {u.posts}')

def session():
    while True:
        ofor()
        print('''Возможные действия:
        - ПОДПИСКИ
        - ПОДПИСЧИКИ
        - ПОДПИСАТЬСЯ
        - СЛЕДУЮЩИЙ АККАУНТ''')


a = Person('чак', 'чак')
b = Person('leonya', 'ognev', '228', 'L')
c = Person()
d = Person()
e = Person()
users = [a, b, c, d, e]
print(ofor())
lg = input('скажи логин:')
ps = input('скажи пароль:')
for i in users:
    if i.log_in(lg, ps) == True:
        session()


