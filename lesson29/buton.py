from tkinter import *

def active():
    if btn1['state'] == 'disabled': # если кнопка выключна
        btn1['state'] = 'normal'
    else:
        btn1['state'] = 'disabled'

root = Tk()

btn1 = Button(root, text='я кнопка!', state='disabled')
btn2 = Checkbutton(root, text='активатор виндовс2023', command=active)
btn2.select()

btn1.pack()
btn2.pack()

root.mainloop()