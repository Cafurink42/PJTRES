import sys 

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk 


root = tk.Tk()

def Btn():
    print ("Oh ! Do you click on the button !!!")
    print("Congratulations !!!")
    print (btn)
def Btn_2():
    print (btn_2)
def result():
    resultado = btn + btn_2
    print ('O resultado é {}:'.format(resultado))

btn  = tk.Button (root, text = '1', bg = 'green', fg = 'black', command=Btn ) 
btn.place(x= 200, y = 200)
btn_2  = tk.Button (root,  text = '2', bg ='red', fg = 'black' , command = Btn_2) 
btn_2.place(x = 100, y = 200)
result  = tk.Button(root, text = '=', bg ='blue', fg ='black', command = result )
result.place(x = 300, y = 200)
btn = 1
btn_2 = 2

root.geometry('500x500')
root.mainloop()