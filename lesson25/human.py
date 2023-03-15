class Human:
    default_name = "имя"
    default_age = 0

    def __init__(self, name = default_name, age = default_age, money = 0, house = "no"):
        self.name = name
        self.age = age
        self.__house = house
        self.__money = money
        self.dom = 'дома нет'
    def info(self):
        return self.name, self.age, self.__house, self.__money

    def earn_money(self):
        self.__money += 1_000_000_000

    def default_info(self):
        return Human.default_age, Human.default_name

    def make_deal(self, dom, dom_prise):
        self.__money -= dom_prise
        self.dom = dom
        dom.owner = self.name
        return dom

    def buy_house(self, dom, dom_prise):
        if self.__money >= dom_prise:
            self.make_deal(dom, dom_prise)
        else:
            return "ты лох! денег у тебя нет!"


