class House:
    def __init__(self, area, prise):
        self.__area = area
        self.__price = prise
    def final_prise(self, ass):
        return self.__price - (self.__price / 100 * ass)