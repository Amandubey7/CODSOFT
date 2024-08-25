import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Initialize the contact list
contacts = {}

def add_contact():
    name = simpledialog.askstring("Input", "Enter contact name:")
    if name in contacts:
        messagebox.showerror("Error", "Contact already exists.")
        return
    
    phone = simpledialog.askstring("Input", "Enter phone number:")
    email = simpledialog.askstring("Input", "Enter email address:")
    address = simpledialog.askstring("Input", "Enter address:")
    
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    update_contact_list()

def view_contacts():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

def update_contact():
    name = simpledialog.askstring("Input", "Enter the name of the contact to update:")
    if name not in contacts:
        messagebox.showerror("Error", "Contact not found.")
        return
    
    phone = simpledialog.askstring("Input", "Enter new phone number (leave empty to keep current):")
    email = simpledialog.askstring("Input", "Enter new email address (leave empty to keep current):")
    address = simpledialog.askstring("Input", "Enter new address (leave empty to keep current):")
    
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address
    
    update_contact_list()

def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone number to search:")
    if not query:
        return
    
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        if query in name or query in details['phone']:
            contact_list.insert(tk.END, f"{name} - {details['phone']}")

def delete_contact():
    name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
    if name not in contacts:
        messagebox.showerror("Error", "Contact not found.")
        return
    
    del contacts[name]
    update_contact_list()

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

# Create the main window
root = tk.Tk()
root.title("Contact Manager")

# Create and place widgets
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="View Contacts", command=view_contacts).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

contact_list = tk.Listbox(root, width=50, height=15)
contact_list.pack(pady=10)

# Run the application
root.mainloop()
