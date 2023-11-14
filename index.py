import sys 

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk 
  

root = tk.Tk()

def btn(button):
    if button == "Pizza":
        output.config(text = 'Você não é nada saudável coleguinha !')

    elif button ==  "Abobora":
        output.config(text = 'Você é muito saudável coleguinha ! Parabéns !!!')


question = tk.Label(root, text = 'O que você mais gosta de comer ?' , bg = 'blue')
question.pack()

answer_one = tk.Button(root, text  ='Pizza', bg ='red', command=lambda: btn("Pizza"))
answer_one.pack()
answer_two = tk.Button(root, text  ='Abobora', bg = 'orange', command=lambda:btn("Abobora")) #lambda passa argumento para a função
                                                                                             #quando for chamado o botão
answer_two.pack()

output = tk.Label(root, text = '', bg = 'white' , width=100, height=40)
output.pack()




root.geometry('500x500')
root.mainloop()