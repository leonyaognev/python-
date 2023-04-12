from tkinter import *

def geterb():
    print(cb_val.get())

root = Tk()
root.geometry('200x250')

cb_val = IntVar()
Radiobutton(root,
            variable=cb_val,
            text='просто батон',
            value=200,
            command=geterb).pack()
Radiobutton(root,
            variable=cb_val,
            text='радиоактивный батон',
            value=500,
            command=geterb).pack()
Radiobutton(root,
            variable=cb_val,
            text='хлебушек бородинский',
            value=10,
            command=geterb).pack()

root.mainloop()