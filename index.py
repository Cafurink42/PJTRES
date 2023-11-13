import sys 

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk 


root = tk.Tk()

def Btn():
    print ("Oh ! Do you click on the button !!!")
    print("Congratulations !!!")
btn  = tk.Button (root, text = 'Click Here', bg = 'green', fg = 'black', command=Btn ) 


btn.place(x= 200, y = 200)
root.geometry('500x500')
root.mainloop()