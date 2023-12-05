import sys 

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk 
  


root = tk.Tk()




question = tk.Label(root, text = 'Write what you like eat ' , bg = 'blue')
question.pack()

def getData():
    getdata = str(data.get())
    Entry = getdata
    if Entry == 'Pizza':
        output.config(text = 'Nothing Health')
    else:
        output.config(text = '{} Very Health ! Congratulations !!'.format(Entry))

data = tk.Entry(root,  bg  = 'yellow')
data.pack()
btn = tk.Button(root, text  = 'send', command=getData)
btn.pack()

output = tk.Label(root, text = '', bg = 'white' , width=100, height=40)
output.pack()

root.geometry('500x500')
root.title('HealfhCARE')

root.mainloop()



