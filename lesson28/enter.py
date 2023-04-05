import tkinter as tk

def mas(event):
    print(ent.get(), txt.get(1.0, 'end'))
    ent.delete(0, 'end')
    txt.delete(1.0, 'end')



root = tk.Tk()
root.configure(background='yellow3')

lb = tk.Label(text='ваш адрес:',
              background='yellow')
lb1 = tk.Label(text='ваш комментарий',
               background='yellow')
ent = tk.Entry(root,
               background='yellow')
btn = tk.Button(root,
                text='отправить',
                background='blue')
txt = tk.Text(root,
              width='20',
              height='5')
btn.bind('<Button-1>', mas)
ent.bind('<Return>', mas)
txt.bind('<Return>', mas)

lb.pack()
ent.pack()
lb1.pack()
txt.pack()
btn.pack()

root.mainloop()