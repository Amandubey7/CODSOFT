import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, include_special_chars):
    """Generate a random password of specified length."""
    if length <= 0:
        messagebox.showerror("Input Error", "Length must be a positive integer.")
        return ""
    
    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(length_entry.get())
        include_special_chars = special_chars_var.get()
        
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        password = generate_password(length, include_special_chars)
        password_var.set(password)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

special_chars_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, width=50, state='readonly')
password_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
