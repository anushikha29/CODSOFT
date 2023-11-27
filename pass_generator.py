import tkinter as tk
import random

def generate_pass():
    length = int(length_entry.get())
    length = max(length, 4)
    char = ""
    
    if lowercase.get():
        char += "abcdefghijklmnopqrstuvwxyz"

    if uppercase.get():
        char += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if numbers.get():
        char += "1234567890"
    
    if symbols.get():
        char += "!@#$%^&*()>:<{,}[\]"

    pass_list = random.sample(char, length)
    random.shuffle(pass_list)
    
    password = ''.join(pass_list)
    
    return password


window = tk.Tk()
window.title("Password Generator")
window.geometry("500x400")
window.configure(bg='lightblue')

letters = tk.Label(window, text="Enter the number of letters you want in your password:")
letters.pack(pady=10)

length_entry = tk.Entry(window, width=7)
length_entry.insert(0, "8")
length_entry.pack(pady=10)

which_letters = tk.Label(window, text="Tick the checkboxes according to your need :)")
which_letters.pack(pady=10)

lowercase= tk.BooleanVar()
uppercase= tk.BooleanVar()
numbers = tk.BooleanVar()
symbols = tk.BooleanVar()

tk.Checkbutton(window, text="Lowercase", variable=lowercase).pack()
tk.Checkbutton(window, text="Uppercase", variable=uppercase).pack()
tk.Checkbutton(window, text="Numbers", variable=numbers).pack()
tk.Checkbutton(window, text="Symbols", variable=symbols).pack()

def generate_pass_function():
    password = generate_pass()
    generated_pass.insert(0, password)

generate_pass_button = tk.Button(window, text=" Click here to generate pass", command=generate_pass_function)
generate_pass_button.pack(pady=10)


generated = tk.Label(window, text="Your generated password is: ")
generated.pack(pady=10)

generated_pass = tk.Entry(window, width=10)
generated_pass.pack(padx=10, pady=10)


window.mainloop()
