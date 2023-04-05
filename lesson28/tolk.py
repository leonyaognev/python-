import tkinter as tk

def bah():
    lab1['image'] = tk.PhotoImage(file='AAA1.png').zoom(1, 5)

root = tk.Tk()

root.title('ЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ')
root.geometry('500x500')

photo = tk.PhotoImage(file='AAA.png').subsample(1, 5)
lab1 = tk.Label(master=root, image=photo)
tk.Button(text='бахнуть толчек', command=bah).pack()

lab1.pack()

root.mainloop()