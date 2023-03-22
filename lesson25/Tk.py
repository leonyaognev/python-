from tkinter import *
from mine import *

def bt1():
    Label(text=chel.buy_house(small, small.final_prise(0))).pack()
def bt2():
    Label(text=chel.buy_house(normal, normal.final_prise(0))).pack()
def bt3():
    Label(text=chel.buy_house(big, big.final_prise(0))).pack()
def bt4():
    chel.earn_money()



root = Tk()

root.geometry("500x250")
Label(text = f'''у нас есть три дома какой нужен тебе?
1)маленький, далеко от работы, стоит 1_000_000_000
2)нормальный по площади дом, ближе к работе, стоит 5_000_000_000
3)большой дом, бизко к работе стоит 10_000_000_000

''').pack()
btn1 = Button(text = '''дом1''', command = bt1)
btn2 = Button(text = '''дом2''', command = bt2)
btn3 = Button(text = '''дом3''', command = bt3)
btn4 = Button(text = '''сходи поработай''', command = bt4)
btn1.pack(), btn2.pack(), btn3.pack(), btn4.pack(anchor='se')

root.mainloop()


