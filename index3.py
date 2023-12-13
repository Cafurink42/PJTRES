from random import * 
import tkinter as tk  

root  = tk.Tk()

def Teams():
    if len(player_list) < maxplayers:
            getName = (PlayeresNames.get())
            player_list.append(getName)
            update_output()
    if getName == "":
          output.config (text = 'Parece que você não digitou nenhum jogador. Por favor insira algum jogador')          

def SortTeams():
      shuffle(player_list)
      update_output()

def update_output():
      output.config(text = ','.join(player_list))




title = tk.Label(root, text  = 'Insert your team')
title.pack()
PlayeresNames = tk.Entry(root, bg = 'gray')
PlayeresNames.pack()
FormTeams =  tk.Button(root, text = 'Send Player', command  = Teams)
FormTeams.pack()
Sortteam = tk.Button(root, text = 'Sort Team', command  = SortTeams)
Sortteam.pack()


output = tk.Label(root, bg = 'yellow', width= 80, height=10)
output.pack()

player_list = []
maxplayers  = 6




root.title('Add Teams')
root.geometry('500x600')
root.config(background= 'green')
root.mainloop()
