from tkinter import *

def pupu():
    print(lstbox.curselection())

root = Tk()

list = ['боба', 'жорик', 'и', 'пивас']
lstbox = Listbox(root,
                 selectmode=EXTENDED)
for i in list:
    lstbox.insert("end", i)

Button(root,
       text='Активировать',
       command=pupu).pack()

lstbox.pack()

root.mainloop()