
from random import * 

import sys 

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk 


root = tk.Tk()

def btn():
    getInsert = int (InserNum.get())
    randomNum = round(random())
    print(randomNum)
    if getInsert == randomNum:
        output.config(text = 'Very Lucky ! ')
    else:
        output.config(text = 'Bad Lucky :( ')
        

title = tk.Label(root, text = 'Try the Lucky ')
title.place(x = 170, y = 0)
InserNum = tk.Entry(root, bg = 'gray')
InserNum.place(x = 170, y = 20)
bt = tk.Button(root, text = 'Send', command=btn)
bt.place(x = 170, y  = 70)
output  = tk.Label(root, text = '', width= 50, height= 10, bg  = 'green')
output.place(x = 50, y = 120)





root.title('Bad or Lucky')
root.geometry('500x450')
root.mainloop()
