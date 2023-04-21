from tkinter import *
ass = 0
c = 0
def xo(event):
    pass
    # global ass
    # global c
    # if event['text'] == '':
    #     if ass % 2 == 0:
    #         event['text'] = 'x'
    #         print(c)
    #     else:
    #         event['text'] = '0'
    #     ass += 1
    #     c += 1
    #     print(c)
    #     if c == 14:
    #         print("Леня ну ебаный рот")
    #         exit()
        # if [bat1['text'], bat2['text'], bat3['text']] == ['x','x','x'] or [bat4['text'], bat5['text'], bat6['text']] == ['x','x','x'] or [bat7['text'], bat8['text'], bat9['text']] == ['x','x','x'] or [bat1['text'], bat4['text'], bat7['text']] == ['x','x','x'] or [bat2['text'], bat5['text'], bat8['text']] == ['x','x','x'] or [bat3['text'], bat6['text'], bat9['text']] == ['x','x','x'] or [bat1['text'], bat5['text'], bat9['text']] == ['x','x','x'] or [bat3['text'], bat5['text'], bat7['text']] == ['x','x','x']:
        #     print('ВЫИГРАЛИ КРЕСТИКИ!!!!!')
        #     exit()
        # elif [bat1['text'], bat2['text'], bat3['text']] == ['0','0','0'] or [bat4['text'], bat5['text'], bat6['text']] == ['0','0','0'] or [bat7['text'], bat8['text'], bat9['text']] == ['0','0','0'] or [bat1['text'], bat4['text'], bat7['text']] == ['0','0','0'] or [bat2['text'], bat5['text'], bat8['text']] == ['0','0','0'] or [bat3['text'], bat6['text'], bat9['text']] == ['0','0','0'] or [bat1['text'], bat5['text'], bat9['text']] == ['0','0','0'] or [bat3['text'], bat5['text'], bat7['text']] == ['0','0','0']:
        #     print('ВЫИГРАЛИ НОЛИКИ!!!!!')
        #     exit()
def restart():
    global ass, c
    # bat1['text'] = ''
    # bat2['text'] = ''
    # bat3['text'] = ''
    # bat4['text'] = ''
    # bat5['text'] = ''
    # bat6['text'] = ''
    # bat7['text'] = ''
    # bat8['text'] = ''
    # bat9['text'] = ''
    ass = 0
    с = 0

lst = list()
i = 0
root = Tk()


for row in range(3):
    for column in range(3):
        lst.append(Button(width=3, text='сукибляди'))
        lst[i].bind('<Button-1>', lambda event: xo(lst[i]))
        lst[i].grid(row=row, column=column)
        print(lst[i]['func'])
        i += 1


# bat1 = Button(width=3)
# bat2 = Button(width=3)
# bat3 = Button(width=3)
# bat4 = Button(width=3)
# bat5 = Button(width=3)
# bat6 = Button(width=3)
# bat7 = Button(width=3)
# bat8 = Button(width=3)
# bat9 = Button(width=3)
# bat1.bind('<Button-1>', lambda event: xo(bat1))
# bat2.bind('<Button-1>', lambda event: xo(bat2))
# bat3.bind('<Button-1>', lambda event: xo(bat3))
# bat4.bind('<Button-1>', lambda event: xo(bat4))
# bat5.bind('<Button-1>', lambda event: xo(bat5))
# bat6.bind('<Button-1>', lambda event: xo(bat6))
# bat7.bind('<Button-1>', lambda event: xo(bat7))
# bat8.bind('<Button-1>', lambda event: xo(bat8))
# bat9.bind('<Button-1>', lambda event: xo(bat9))
# bat1.grid(row=0, column=1)
# bat2.grid(row=0, column=2)
# bat3.grid(row=0, column=3)
# bat4.grid(row=1, column=1)
# bat5.grid(row=1, column=2)
# bat6.grid(row=1, column=3)
# bat7.grid(row=2, column=1)
# bat8.grid(row=2, column=2)
# bat9.grid(row=2, column=3)


root.mainloop()
