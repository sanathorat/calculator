# calculator 


import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")

display = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)

expression = ""

def button_click(item):
    global expression
    expression += str(item)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def button_clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def button_equal():
    global expression
    try:
        result = str(eval(expression))  
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result  
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: button_click(x) if x not in ['C', '='] else (button_clear() if x == 'C' else button_equal())
    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()

