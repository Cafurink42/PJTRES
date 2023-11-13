import sys 

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk 


root = tk.Tk()

def Btn():
    print ('Click btn ')

btn  = tk.Button (root, text = 'Click Here', bg = 'green', fg = 'black', command=Btn ) 
btn.pack()
root.geometry('500x500')
root.mainloop()