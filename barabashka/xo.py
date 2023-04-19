from tkinter import *
from PIL import Image

ass = 0

x = Image.open('крест.png')

def xo(event):
    global ass
    if event['text'] == '':
        if ass % 2 == 0:
            event['text'] = 'x'
            if [bat1['text'], bat2['text'], bat3['text']] == ['x','x','x'] or [bat4['text'], bat5['text'], bat6['text']] == ['x','x','x'] or [bat7['text'], bat8['text'], bat9['text']] == ['x','x','x'] or [bat1['text'], bat4['text'], bat7['text']] == ['x','x','x'] or [bat2['text'], bat5['text'], bat8['text']] == ['x','x','x'] or [bat3['text'], bat6['text'], bat9['text']] == ['x','x','x'] or [bat1['text'], bat5['text'], bat9['text']] == ['x','x','x'] or [bat3['text'], bat5['text'], bat7['text']] == ['x','x','x']:
                print('ВЫИГРАЛИ КРЕСТИКИ!!!!!')
                bat1['text'] = ''
                bat2['text'] = ''
                bat3['text'] = ''
                bat4['text'] = ''
                bat5['text'] = ''
                bat6['text'] = ''
                bat7['text'] = ''
                bat8['text'] = ''
                bat9['text'] = ''
            elif [bat1['text'], bat2['text'], bat3['text']] == ['0','0','0'] or [bat4['text'], bat5['text'], bat6['text']] == ['0','0','0'] or [bat7['text'], bat8['text'], bat9['text']] == ['0','0','0'] or [bat1['text'], bat4['text'], bat7['text']] == ['0','0','0'] or [bat2['text'], bat5['text'], bat8['text']] == ['0','0','0'] or [bat3['text'], bat6['text'], bat9['text']] == ['0','0','0'] or [bat1['text'], bat5['text'], bat9['text']] == ['0','0','0'] or [bat3['text'], bat5['text'], bat7['text']] == ['0','0','0']:
                print('ВЫИГРАЛИ НОЛИКИ!!!!!')
                bat1['text'] = ''
                bat2['text'] = ''
                bat3['text'] = ''
                bat4['text'] = ''
                bat5['text'] = ''
                bat6['text'] = ''
                bat7['text'] = ''
                bat8['text'] = ''
                bat9['text'] = ''
            elif [bat1['text'], bat2['text'], bat3['text'], bat4['text'], bat5['text'], bat6['text'], bat7['text'], bat8['text'], bat9['text']] != ['', '', '', '', '', '', '', '']:
                print('НЕЧЬЯ!!!!!!!')
                bat1['text'] = ''
                bat2['text'] = ''
                bat3['text'] = ''
                bat4['text'] = ''
                bat5['text'] = ''
                bat6['text'] = ''
                bat7['text'] = ''
                bat8['text'] = ''
                bat9['text'] = ''
        else:
            event['text'] = 'o'
        ass += 1

root = Tk()

bat1 = Button(width=3)
bat2 = Button(width=3)
bat3 = Button(width=3)
bat4 = Button(width=3)
bat5 = Button(width=3)
bat6 = Button(width=3)
bat7 = Button(width=3)
bat8 = Button(width=3)
bat9 = Button(width=3)

bat1.bind('<Button-1>', lambda event: xo(bat1))
bat2.bind('<Button-1>', lambda event: xo(bat2))
bat3.bind('<Button-1>', lambda event: xo(bat3))
bat4.bind('<Button-1>', lambda event: xo(bat4))
bat5.bind('<Button-1>', lambda event: xo(bat5))
bat6.bind('<Button-1>', lambda event: xo(bat6))
bat7.bind('<Button-1>', lambda event: xo(bat7))
bat8.bind('<Button-1>', lambda event: xo(bat8))
bat9.bind('<Button-1>', lambda event: xo(bat9))

bat1.grid(row=0, column=1)
bat2.grid(row=0, column=2)
bat3.grid(row=0, column=3)
bat4.grid(row=1, column=1)
bat5.grid(row=1, column=2)
bat6.grid(row=1, column=3)
bat7.grid(row=2, column=1)
bat8.grid(row=2, column=2)
bat9.grid(row=2, column=3)

root.mainloop()