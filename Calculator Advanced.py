import tkinter as tk
from tkinter import messagebox
import math

def calculate(event=None):
    try:
        # Replace visual symbols with python operators
        expression = entry.get().replace('×', '*').replace('÷', '/')
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid Expression")
        entry.delete(0, tk.END)

def on_click(text):
    if text == "=":
        calculate()
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "⌫": # Backspace
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])
    elif text == "√":
        try:
            val = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(math.sqrt(val)))
        except:
            messagebox.showerror("Error", "Invalid Input for √")
    elif text == "x²":
        try:
            val = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(val**2))
        except:
            messagebox.showerror("Error", "Invalid Input")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Pro Calculator")
root.configure(bg="#2c3e50") # Dark theme background

# Styling configuration
btn_params = {'font': ("Arial", 12, "bold"), 'bd': 0, 'fg': "#ecf0f1", 'bg': "#34495e", 'width': 5, 'height': 2}

entry = tk.Entry(root, font=("Arial", 24), bg="#ecf0f1", fg="#2c3e50", borderwidth=10, relief="flat", justify='right')
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=20)

buttons = [
    '7', '8', '9', '÷', '⌫',
    '4', '5', '6', '×', '√',
    '1', '2', '3', '-', 'x²',
    'C', '0', '.', '+', '='
]

row_val, col_val = 1, 0
for button in buttons:
    # Color coding special buttons
    current_params = btn_params.copy()
    if button == "=": current_params['bg'] = "#27ae60"
    if button == "C": current_params['bg'] = "#e74c3c"
    if button in ['÷', '×', '-', '+', '√', 'x²', '⌫']: current_params['bg'] = "#8e44ad"

    action = lambda x=button: on_click(x)
    tk.Button(root, text=button, **current_params, command=action).grid(row=row_val, column=col_val, padx=2, pady=2)
    
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

root.bind('<Return>', calculate)
root.mainloop()