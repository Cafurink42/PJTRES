import sys 

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk 
  

root = tk.Tk()

def btn():
    if answer_one:
        output.config(text = 'Você não é nada saudável coleguinha !')

def btnBad():

    if answer_two:
        output.config(text = 'Você é muito saudável coleguinha ! Parabéns !!!')


question = tk.Label(root, text = 'O que você mais gosta de comer ?' , bg = 'blue')
question.pack()

answer_one = tk.Button(root, text  ='Pizza', bg ='red', command=btn)
answer_one.pack()
answer_two = tk.Button(root, text  ='Abobora', bg = 'orange', command = btnBad)
answer_two.pack()

output = tk.Label(root, text = '', bg = 'white' , width=100, height=40)
output.pack()




root.geometry('500x500')
root.mainloop()