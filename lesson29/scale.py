from tkinter import *

def get_scale(e):
    print(scal.get())

root = Tk()

scal = Scale(root,
             from_=0,
             to=9999999999999999999999999999999999999999999999999999999999,
             orient=HORIZONTAL,
             length=1950,
             width=400,
             tickinterval=2,
             command=get_scale)
scal.pack()

root.mainloop()
