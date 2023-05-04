from tkinter import *

def deistvie1():
    try: lt[0][4].delete(0, END), lt[0][4].insert(0, int(lt[0][0].get()) + int(lt[0][2].get()))
    except: print('ошибка')
def deistvie2():
    try: lt[1][4].delete(0, END), lt[1][4].insert(0, int(lt[1][0].get()) - int(lt[1][2].get()))
    except: print('ошибка')
def deistvie3():
    try: lt[2][4].delete(0, END), lt[2][4].insert(0, int(lt[2][0].get()) * int(lt[2][2].get()))
    except: print('ошибка')
def deistvie4():
    try: lt[3][4].delete(0, END), lt[3][4].insert(0, int(lt[3][0].get()) ** int(lt[3][2].get()))
    except: print('ошибка')
def deistvie5():
    try: lt[4][4].delete(0, END), lt[4][4].insert(0, int(lt[4][0].get()) / int(lt[4][2].get()))
    except: print('ошибка')
def deistvie6():
    try: lt[5][4].delete(0, END), lt[5][4].insert(0, int(lt[5][0].get()) // int(lt[5][2].get()))
    except: print('ошибка')
def deistvie7():
    try: lt[6][4].delete(0, END), lt[6][4].insert(0, int(lt[6][0].get()) % int(lt[6][2].get()))
    except: print('ошибка')

const = (("Сложение", "+", deistvie1),
 ("Вычитание", "-", deistvie2),
 ("Умножение", "*", deistvie3),
 ("Степень", "**", deistvie4),
 ("Деление", "/", deistvie5),
 ("Деление(целая часть)", "//", deistvie6),
 ("Деление(остаток)", "%", deistvie7))

root =Tk()
ls = [LabelFrame(root, text=const[i][0]) for i in range(7)]
lt = [(Entry(master=ls[i]), Label(master=ls[i], text=const[i][1]), Entry(master=ls[i]), Button(master=ls[i], text='=', command=const[i][2]), Entry(master=ls[i])) for i in range(7)]
for i in ls: i.pack()
  foriin lt:
    for j in i:
        j.pack(side=LEFT)
root.mainloop()