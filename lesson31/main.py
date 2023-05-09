# from tkinter import *
#
# a = 1
# def tme():
#     global a
#     can.delete('all')
#     can.create_text(250, 250, text=a, font='Arial 30')
#     a+=1
#     root.after(1000, tme)
#
# root = Tk()
# root.geometry('550x550')
#
# im = PhotoImage(file='ss.png')
# can = Canvas(root, width=500, height=500, bg='white')
#
# can.pack(anchor=CENTER, expand=True)
# tme()
#
# root.mainloop()
#==============================================

from tkinter import *

def banan(event):
    can.create_rectangle(event.x, event.y, event.x+1, event.y+1, width=2)
    print(event.x, event.y)
def AAA(event):
    root.bind('<Motion>', banan)
def BBB(event):
    root.unbind('<Motion>')

root = Tk()
# root.geometry('550x550')

can = Canvas(root, width=500, height=500, bg='white')
root.bind('<ButtonPress>', AAA)
root.bind('<ButtonRelease>', BBB)
can.pack(anchor=CENTER, expand=True)

root.mainloop()