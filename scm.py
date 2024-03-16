import tkinter as tk
import math

def evaluate_expression():
    try:
        result = eval(entry.get())
        output_label.config(text="Result: " + str(result))
    except Exception as e:
        output_label.config(text="Error: " + str(e))

def clear_entry():
    entry.delete(0, tk.END)
    output_label.config(text="Result: ")

def sin_function():
    try:
        angle = float(entry.get())
        result = math.sin(math.radians(angle))
        output_label.config(text="sin(" + str(angle) + ") = " + str(result))
    except ValueError:
        output_label.config(text="Error: Invalid input")

def cos_function():
    try:
        angle = float(entry.get())
        result = math.cos(math.radians(angle))
        output_label.config(text="cos(" + str(angle) + ") = " + str(result))
    except ValueError:
        output_label.config(text="Error: Invalid input")

def tan_function():
    try:
        angle = float(entry.get())
        result = math.tan(math.radians(angle))
        output_label.config(text="tan(" + str(angle) + ") = " + str(result))
    except ValueError:
        output_label.config(text="Error: Invalid input")

root = tk.Tk()
root.title("Simple Scientific Calculator")

entry = tk.Entry(root, width=40, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_list = [
    ('sin', sin_function), ('cos', cos_function), ('tan', tan_function),
    ('7', lambda: entry.insert(tk.END, '7')), ('8', lambda: entry.insert(tk.END, '8')),
    ('9', lambda: entry.insert(tk.END, '9')), ('/', lambda: entry.insert(tk.END, '/')),
    ('4', lambda: entry.insert(tk.END, '4')), ('5', lambda: entry.insert(tk.END, '5')),
    ('6', lambda: entry.insert(tk.END, '6')), ('', lambda: entry.insert(tk.END, '')),
    ('1', lambda: entry.insert(tk.END, '1')), ('2', lambda: entry.insert(tk.END, '2')),
    ('3', lambda: entry.insert(tk.END, '3')), ('-', lambda: entry.insert(tk.END, '-')),
    ('0', lambda: entry.insert(tk.END, '0')), ('.', lambda: entry.insert(tk.END, '.')),
    ('+', lambda: entry.insert(tk.END, '+')), ('Clear', clear_entry),
    ('=', evaluate_expression)
]

row = 1
col = 0
for (text, command) in button_list:
    btn = tk.Button(root, text=text, width=10, height=2, font=('Arial', 12),
                    command=command)
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

output_label = tk.Label(root, text="Result: ", width=40, anchor='w', font=('Arial', 14))
output_label.grid(row=row, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()