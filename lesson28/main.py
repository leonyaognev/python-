import tkinter as tk

def hello(event):
    print('event=', event)
    print('опять hello world')

root = tk.Tk()

root.title('ЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ')
root.geometry('500x500')

photo = tk.PhotoImage(file='AAA.png').subsample(1, 5)
lab1 = tk.Label(master=root, image=photo)
btn = tk.Button(root,
                text='барабашка',
                font=('times new roman', 14, 'bold'),
                height='2',
                width='10',
                background='pink',
                foreground='blue3') #master - привязка к окну
# btn['command'] = hello #изменение действия при нажатии

btn.bind('<Button-1>', hello) #нажатие на левую кнопку мыши
btn.bind('<Button-2>', hello) #нажатие на колесико
btn.bind('<Button-3>', hello) #нажатие на правую кнопку мыши
btn.bind('<Double-Button-3>', hello) #двойное нажатие на левую\правую\среднюю кнопку мыши
btn.bind('<Return>', hello) #нажатие на Enter

# btn['text'] = 'бадабум'

btn.pack(anchor='center')
lab1.pack()

root.mainloop()