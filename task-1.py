import tkinter as tk
from tkinter import messagebox, ttk

def create_task():
    task = task_field.get()
    if task:
        listbox.insert(tk.END, task)
        task_field.delete(0, tk.END)
    else:   	
        messagebox.showinfo("ERROR", "Field is empty, please enter a task!")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showinfo("Error", "Field is empty, please select a task to delete!")

def clear_all_tasks():
    listbox.delete(0, tk.END)

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

if __name__ == "_main_":
    root = tk.Tk()
    root.title("TO-DO LIST APPLICATION")
    root.geometry("600x700+700+500")
    root.resizable(0, 0)
    root.configure(bg="#FACAD7")

    task_field = tk.Entry(root, font=("Helvetica", 14))
    task_field.pack(pady=20)

    create_button = tk.Button(root, text="Add Task", command=create_task)
    create_button.pack()

    delete_button = tk.Button(root, text="Delete Task", command=delete_task)
    delete_button.pack()

    clear_button = tk.Button(root, text="Clear All", command=clear_all_tasks)
    clear_button.pack()

    save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
    save_button.pack()

    listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 12), bg="#FAF807")
    listbox.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
