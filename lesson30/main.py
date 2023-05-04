from tkinter import *

def deistvie1(ind):
    try: exec(f'lt[ind][4].delete(0, END), lt[ind][4].insert(0, int(lt[ind][0].get()) {const[ind][1]} int(lt[ind][2].get()))')
    except: print('ошибка')

const = (("Сложение", "+"),
         ("Вычитание", "-",),
         ("Умножение", "*"),
         ("Степень", "**"),
         ("Деление", "/"),
         ("Деление(целая часть)", "//"),
         ("Деление(остаток)", "%"))

root = Tk()
ls = [LabelFrame(root, text=const[i][0]) for i in range(7)]
lt = [(Entry(master=ls[i]), Label(master=ls[i], text=const[i][1]), Entry(master=ls[i]), Button(master=ls[i], text='='), Entry(master=ls[i])) for i in range(7)]
for i in ls: i.pack()
for b, i in enumerate(lt):
    exec(f'a{b} = b')
    exec(f"i[3].bind('<Button-1>', lambda ind: deistvie1(a{b}))")
    for j in i:
        j.pack(side=LEFT)
root.mainloop()