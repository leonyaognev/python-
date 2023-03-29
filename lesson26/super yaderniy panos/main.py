from Person import Person
import random


def ofor():
    print(f'логин: {u.login}')
    print(f'имя: {u.name}')
    print(f'фамилия: {u.surname}')
    print(f'посты: {u.posts}')

def select_usr():
    # global u
    # u = random.choice(users)
    # while True:
    #     if u.login == current.login: #если выбрали сами себя
    #         u = random.choice(users)
    #     else:
    #         break
    global u
    while True:
        u = random.choice(users)
        if u.login != current.login:
            break

def session():
    select_usr()
    while True:
        ofor()
        print('''Возможные действия:
        - ПОДПИСКИ
        - ПОДПИСЧИКИ
        - ПОДПИСАТЬСЯ
        - СЛЕДУЮЩИЙ АККАУНТ''')
        spros = input(('> ')).upper()
        if spros == 'ВЫХОД':
            break
        elif spros == 'СЛЕДУЮЩИЙ':
            continue
        elif spros == 'ПОДПИСАТЬСЯ':
            current.subsscribe += 1
            u.subsscribes +=1


a = Person('чак', 'чак')
b = Person('leonya', 'ognev', '228', 'L')
c = Person()
d = Person()
e = Person()
users = [a, b, c, d, e]
lg = input('скажи логин:')
ps = input('скажи пароль:')
for i in users:
    if i.log_in(lg, ps) == True:
        current = i
        session()
print(i.name)


