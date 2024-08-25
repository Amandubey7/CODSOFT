import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Create a frame for the listbox and scrollbar
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Create the listbox to display tasks
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE, activestyle="none")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Create a scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the scrollbar and listbox
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Create the entry box for new tasks
        self.task_entry = tk.Entry(root, width=52)
        self.task_entry.pack(pady=10)

        # Create the buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.complete_task)
        self.complete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(tk.END, f"{task} (Completed)")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
