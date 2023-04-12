from tkinter import *
#
# def chb(event):
#     print(cb_val.get())
#     chek.deselect() # снять выделение
#     chek.select() # поствить выдление
#
# root = Tk()
# root.geometry('500x500')
#
# cb_val = BooleanVar() # переменная хранящая значение
# chek = Checkbutton(root,
#                    text='чекбатон',
#                    variable=cb_val,
#                    onvalue=True,
#                    offvalue=False)
# chek.bind('<Button-3>', chb)
#
# chek.pack()
#
# root.mainloop()
#=======================================

# def wp():
#     print(val)
#     if val.get() == 1:
#         lab['text'] = 'Hello World'
#     else:
#         lab['text'] = 'Hello Python'
#
# root = Tk()
#
# val = IntVar()
#
# lab = Label(root, text='Hello ...')
# cb1 = Radiobutton(root, text='World', variable=val, value=1, command=wp)
# cb2 = Radiobutton(root, text='Python', variable=val, value=2, command=wp)
#
# lab.pack()
# cb1.pack()
# cb2.pack()
#
# root.mainloop()

# def bold():
#     if val1.get():
#         lb['font'] += ' bold'
#     else:
#         lb['font'] = lb['font'].replace(' bold', '')
# def italic():
#     if val2.get == True:
#         pass
#     else:
#         pass
# def ovestrike():
#     if val3.get == True:
#         pass
#     else:
#         pass
# def anderline():
#     if val4.get == True:
#         pass
#     else:
#         pass
#
# root = Tk()
#
# val1 = BooleanVar()
# lb = Label(root, text='появился как то на зоне черный сталкер',
#            font='Arial 15')
# chek1 = Checkbutton(root,
#                    text='Жирный',
#                    command=bold,
#                    variable=val1,
#                    onvalue=True,
#                    offvalue=False)
# val2 = BooleanVar()
# chek2 = Checkbutton(root,
#                    text='курсив',
#                    command=italic,
#                    variable=val2,
#                    onvalue=True,
#                    offvalue=False)
# val3 = BooleanVar()
# chek3 = Checkbutton(root,
#                    text='зачеркнуутый',
#                    command=ovestrike,
#                    variable=val3,
#                    onvalue=True,
#                    offvalue=False)
# val4 = BooleanVar()
# chek4 = Checkbutton(root,
#                    text='подчеркнутый',
#                    command=anderline,
#                    variable=val4,
#                    onvalue=True,
#                    offvalue=False)
#
# lb.pack()
# chek1.pack()
# chek2.pack()
# chek3.pack()
# chek4.pack()
#
#
# root.mainloop()

# list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# def bg(b):
#     root.config(background=list[scal.get()])
#
#
# root = Tk()
# root.geometry('250x200')
#
# scal = Scale(root,
#              from_=0,
#              to=5,
#              orient=HORIZONTAL,
#              length=200,
#              command=bg)
#
# scal.pack()
#
# root.mainloop()

root = Tk()

ima = PhotoImage(file='уважение.png').subsample()
lab = Label()

root.mainloop()








