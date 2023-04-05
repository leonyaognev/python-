import tkinter as tk

lis = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def zvet():
    pass

root = tk.Tk()

root.title('ЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ')

lb = tk.Label(text='нажмите на цвет')
ent = tk.Entry(root)
btn1 = tk.Button(background='red', width='18')
btn2 = tk.Button(background='orange', width='18')
btn3 = tk.Button(background='yellow', width='18')
btn4 = tk.Button(background='green', width='18')
btn5 = tk.Button(background='blue', width='18')
btn6 = tk.Button(background='purple', width='18')

lb.pack()
ent.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()

root.mainloop()