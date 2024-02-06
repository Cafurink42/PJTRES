from random import * 
import tkinter as tk  

root  = tk.Tk()

def Teams():

    if len(player_list) < maxplayers:
            getName = (PlayeresNames.get())
            player_list.append(getName)
            output.config(text  = '{}'.format(player_list))


def SortTeams():
      shuffle(player_list)
      output.config(text = 'Time sorteado {}'.format(player_list))


bg = tk.PhotoImage(file = "./images/futebolsoccer.png")


labelIMG = tk.Label(root, image = bg)
labelIMG.place(x = 0, y = 0)

title = tk.Label(root, text  = 'Insert your team')
title.pack()
PlayeresNames = tk.Entry(root, bg = 'gray')
PlayeresNames.pack()
FormTeams =  tk.Button(root, text = 'Send', command  = Teams)
FormTeams.pack()
Sortteam = tk.Button(root, text = 'Sort Team', command  = SortTeams)
Sortteam.pack()


output = tk.Label(root, bg = 'yellow', width= 50, height=10)
output.pack()

player_list = []
maxplayers  = 5





root.title('Add Teams')
root.geometry('400x600')
root.config(background= 'green')
root.mainloop()
