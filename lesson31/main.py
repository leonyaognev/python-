from tkinter import *

root = Tk()
root.geometry('550x550')

can = Canvas(root, width=500, height=500, bg='white')
can.create_text(10, 10,
                text='чупапи муняня')

can.pack(anchor=CENTER, expand=True)

root.mainloop()