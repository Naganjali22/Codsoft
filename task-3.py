import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters
    
    if include_digits:
        characters += string.digits
    
    if include_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_click():
    try:
        password_length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
        return
    
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()
    
    password = generate_password(password_length, include_digits, include_special_chars)
    password_label.config(text="Generated Password: " + password)

root = tk.Tk()
root.title("Password Generator")
root.configure(bg="pink")  

heading_label = tk.Label(root, text="Password Generator", fg="purple", font=("Helvetica", 16, "bold"))
heading_label.pack(pady=10)  

username_label = tk.Label(root, text="Enter username:", fg="purple")  
username_label.pack()

username_entry = tk.Entry(root, fg="purple")  
username_entry.pack()

length_label = tk.Label(root, text="Enter password length:", fg="green")  
length_label.pack()


length_entry = tk.Entry(root, fg="green")  
length_entry.pack()

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(root, text="Include digits", variable=digits_var, fg="blue")  
digits_check.pack()

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(root, text="Include special characters", variable=special_chars_var, fg="blue")  
special_chars_check.pack()

accept_button = tk.Button(root, text="Accept", command=generate_password_click, fg="white", bg="blue")  
accept_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=lambda: password_label.config(text=""), fg="white", bg="red")  
reset_button.pack(pady=5)


password_label = tk.Label(root, text="", fg="red")  
password_label.pack()

root.mainloop()
