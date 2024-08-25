import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == 'Add':
            result = num1 + num2
        elif operation == 'Subtract':
            result = num1 - num2
        elif operation == 'Multiply':
            result = num1 * num2
        elif operation == 'Divide':
            result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place widgets
tk.Label(root, text="Number 1:").grid(row=0, column=0)
tk.Label(root, text="Number 2:").grid(row=1, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

operation_var = tk.StringVar(value='Add')

tk.Radiobutton(root, text="Add", variable=operation_var, value='Add').grid(row=2, column=0)
tk.Radiobutton(root, text="Subtract", variable=operation_var, value='Subtract').grid(row=2, column=1)
tk.Radiobutton(root, text="Multiply", variable=operation_var, value='Multiply').grid(row=2, column=2)
tk.Radiobutton(root, text="Divide", variable=operation_var, value='Divide').grid(row=2, column=3)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=4)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=4)

root.mainloop()
