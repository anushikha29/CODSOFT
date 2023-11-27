import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def button_click(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


window = tk.Tk()
window.title("Arithmetic Calculator")
window.configure(bg='#2C3E50')
entry = tk.Entry(window, width=30)
image = Image.open(r"/home/nova/Downloads/backspace.png")
resized_image = image.resize((80, 50), Image.ANTIALIAS)
backspace = ImageTk.PhotoImage(resized_image)
entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10, sticky='nsew')
buttons = [
    ("(", 1, 1), (")", 1, 2), ("+", 1, 3), ("√", 1, 4),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("-", 2, 3), ("x²", 2, 4),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3), ("sin", 3, 4),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("/ ", 4, 3), ("cos", 4, 4),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 4)
]

for button_text, row, column in buttons:
    button = tk.Button(window, text=button_text, width=5,height=2, command=lambda value=button_text: button_click(value),bg="#333333",fg="white")
    button.grid(row=row, column=column,padx=1,pady=1,sticky='nsew')
clear_button = tk.Button(window, image=backspace,width=60,height = 42, command=clear)
clear_button.grid(row=1, column=0, columnspan=1,padx=1,pady=1)
calculate_button = tk.Button(window, text="Calculate", width=15,height=2, command=calculate,bg="#8c8c8c")
calculate_button.grid(row=5, column=2, columnspan = 2,padx=1,pady=1)

window.mainloop()
