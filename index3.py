from random import * 
import tkinter as tk  
from PIL import * 
import random


root  = tk.Tk()

canvas = tk.Canvas(root, width = 400, height=600)
canvas.pack()

def Teams():
    if len(player_list) <= maxplayers:
            getName = (PlayeresNames.get())
            player_list.append(getName)
            output.config(text  = '{}'.format(player_list))

            #faz a listagem de jogadores

def SortTeams():
         shuffle(player_list)

         for i in range (5):
                player = random.choice(player_list)
                x = random.randint(50,400)
                y = random.randint(50, 600)
                canvas.create_text(x, y, text=player, fill = "white", font = ("Arial", 12, "bold"))
                player_list.remove(player)
                

         ##output.config(text = 'Time sorteado {}'.format(player_list))



bg = tk.PhotoImage(file = "./images/futebolsoccer.png")

canvas.create_image(0,0, anchor=tk.NW, image=bg)



title = tk.Label(root, text  = 'Insert your team')
title.pack()

PlayeresNames = tk.Entry(root, bg = 'gray')
PlayeresNames.pack()

FormTeams =  tk.Button(root, text = 'Send', command  = Teams)
FormTeams.pack()

Sortteam = tk.Button(root, text = 'Sort Team', command  = SortTeams)
Sortteam.pack()

output = tk.Label(root, bg = 'yellow', width= 70, height=10)
output.pack()

player_list = []
maxplayers  = 5

root.title('Add Teams')

root.config(background= 'green')
root.mainloop()
