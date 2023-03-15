from tkinter import *
from mine import *

def bt1():
    chel.buy_house(small, small.final_prise(0))
def bt2():
    chel.buy_house(normal, normal.final_prise(0))
def bt3():
    chel.buy_house(big, big.final_prise(0))

root = Tk()

root.geometry("500x250")
Label(text = '''у нас есть три домаБ какой нужен тебе?
1)маленький, далеко от работы, стоит 1_000_000_000
2)нормальный по площади дом, ближе к работе, стоит 5_000_000_000
3)большой дом, бизко к работеБ стоит 10_000_000_000''').pack()
Button(text = '''дом1''', command = bt1).pack()
Button(text = '''дом2''', command = bt2).pack()
Button(text = '''дом3''', command = bt3).pack()

root.mainloop()


