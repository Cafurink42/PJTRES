from random import * 
import tkinter as tk  

def main():
      root  = tk.Tk()
      root.title('Add Teams')
      root.geometry('700x600')
      root.config(background= 'green')



      

      def Teams():
          if len(player_list) < maxplayers:
                  getName = (PlayeresNames.get())
                  player_list.append(getName)
                  update_output()
          if getName == "":
                output.config (text = "Parece que você não digitou nenhum jogador. Por favor insira algum jogador", fg  = "red", font = 16)          
      
      def SortTeams():
            shuffle(player_list)
            update_output()
      
      def update_output():
            output.config(text = ','.join(player_list))
      
      
      bgimg= tk.PhotoImage(file= "images/futebolsoccer.png" )
      #Specify the file name present in the same directory or else
      #specify the proper path for retrieving the image to set it as background image.
      limg= tk.Label(root, i=bgimg, height= 1700, width=1400)
      limg.place(x = -650, y = -1000)
      
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
      maxplayers = 6
      
      
      
      root.mainloop()


if __name__ == "__main__":
      main()
