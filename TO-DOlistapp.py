import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

window = tk.Tk()

window.title("To-Do List")
window.geometry("500x500")
window.configure(bg='#452020')

tasks=[]

image1 = Image.open(r"/home/nova/Downloads/add.png")
image2 = Image.open(r"/home/nova/Downloads/cross.png")
image3 = Image.open(r"/home/nova/Downloads/markasdone.png")
resized_image1 = image1.resize((40, 40), Image.ANTIALIAS)
resized_image2 = image2.resize((40, 40), Image.ANTIALIAS)
resized_image3 = image3.resize((40, 40), Image.ANTIALIAS)
add_image = ImageTk.PhotoImage(resized_image1)
cross_image = ImageTk.PhotoImage(resized_image2)
mark_image = ImageTk.PhotoImage(resized_image3)

def add_new_task():
    new_task_1 = new_task.get()
    if new_task_1:
        tasks.append(new_task)
        task_listbox.insert(tk.END, new_task_1)
        new_task.delete(0, tk.END)

def mark_done():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.itemconfig(selected_task_index, {'bg': 'lightgray'})
    else:
        messagebox.showwarning("Please select a task to mark as done.")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
        del tasks[selected_task_index[0]]
    else:
        messagebox.showwarning("No Task Selected")

add_label = tk.Label(window, text="Enter your tasks here: ")
add_label.grid(row=0,column=0)
new_task = tk.Entry(window, width=40)
new_task.grid(row=1, column=0   , padx=10, pady=10)

add_button = tk.Button(window, image=add_image, command=add_new_task)
add_button.grid(row=0, column=1, padx=5, pady=10)


task_listbox = tk.Listbox(window, width=50, height=10, bg = "#b08787")
task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

done_button = tk.Button(window, image=mark_image, text="Mark as Done", command=mark_done)
done_button.grid(row=3, column=0, padx=5, pady=10)
done_label = tk.Label(window, text="Mark as done: ")

delete_button = tk.Button(window, image=cross_image, text="Delete Task", command=delete_task)
delete_button.grid(row=3, column=1, padx=5, pady=10)



window.mainloop()