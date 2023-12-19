import tkinter as tk
from tkinter import messagebox


class ListTask:
    def __init__(self, master):
        self.master = master
        master.title('ListApp')

        self.task_input = tk.Entry(root, width=30)
        self.task_input.pack(pady=30)

        self.add_button = tk.Button(root, text='add', command=self.add_task)
        self.add_button.pack(pady=5)

        self.button_remove_task = tk.Button(root, text='Remove task', command=self.remove_task)
        self.button_remove_task.pack(pady=5)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30, height=10)
        self.task_listbox.pack(pady=10)

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.task_listbox.insert(tk.END, task)
        else:
            messagebox.showwarning('Warning', 'Please enter a task')

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning('Warning', 'Please select a task to remove')


if __name__ == "__main__":
    root = tk.Tk()
    app = ListTask(root)
    root.mainloop()