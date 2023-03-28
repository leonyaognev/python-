import requests
import random
import json

class Person:
    def __init__(self, name='', surname='', login='', ps=''):
        self.__data = requests.get('https://api.randomdatatools.ru/').json()
        self.lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eu est vel velit faucibus congue. Mauris eleifend turpis sit amet ligula ultrices molestie. Donec finibus dolor ipsum, eget ultrices leo dapibus ut. Donec finibus, neque sit amet ornare efficitur, mi lorem lobortis risus, in sollicitudin dolor mi eu lectus. Sed sed libero consectetur, faucibus elit eget, maximus sapien. Aenean fringilla malesuada orci, vitae placerat metus viverra sed. Sed a tellus semper, lobortis enim non, pretium lectus. Suspendisse egestas ligula nec consequat hendrerit. Pellentesque posuere mattis ante. Sed vehicula justo eget ipsum porttitor consequat. Mauris at lobortis enim.'
        self.name = self.__data['FirstName'] if not name else name
        self.surname = self.__data['LastName'] if not surname else surname
        self.login = self.__data['Login'] if not login else login
        self.__password = self.__data['Password'] if not ps else ps
        self.subsscribe = []
        self.subsscribes = []
        self.posts = [self.lorem[random.randint(1,20): random.randint(20,40)] for i in range(random.randint(0,10))]

    def log_in(self, login, password):
        if self.login == login and self.__password == password:
            return True
        else:
            return False
