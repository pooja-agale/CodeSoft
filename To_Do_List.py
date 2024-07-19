import tkinter as tk
from tkinter import Label
from tkinter import Toplevel

def add_task():
    task = label1_entry.get()
    tasks.append(task)
    task_list.insert(tk.END, task)
    label1_entry.delete(0, tk.END)
    
    
def delete_task():
    selected_index = task_list.curselection()
    if selected_index:
        task_index = selected_index[0]
        delete_task = tasks.pop(task_index)
        task_list.delete(task_index)
        update_task_section()
        

def show_tracked_tasks():
    tracked_window = Toplevel(window)
    tracked_window.title("Tracked Tasks")
    tracked_window.geometry('200x200')
    tracked_tasks_label = tk.Label(tracked_window, text='', font=('Times New Roman', 12))
    tasks_text = "\n".join(tasks)
    tracked_tasks_label.config(text=tasks_text)
    tracked_tasks_label.pack()
    


def update_task_section():
    print("Updating task section....")
    print("Current tasks: ", tasks)
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)


window = tk.Tk()
window.title('WELCOME')
window.geometry('450x450')
window.config(bg='purple')

tasks = []

def close():
    exit()

label = tk.Label(window, text="TO-DO LIST", bg='purple', fg='white', font=('Times New Roman', 15))
label.place(x=150, y=10)

button = tk.Button(window, text='add task', bg='white', fg='black', command = add_task, font=('Times New Roman', 12))
button.place(x=270, y=70)
label1_entry = tk.Entry(window, width=30)
label1_entry.place(x=50, y=80)

task_list = tk.Listbox(width=60, height=12)
task_list.grid(row=1, column=0, columnspan=20, padx=5, pady=20)
task_list.place(x=50, y=130)

button = tk.Button(window, text='update task', bg='white', fg='black', command = update_task_section, font=('Times New Roman', 12))
button.place(x=50, y=350)

button1 = tk.Button(window, text='delete task', bg='white', fg='black', command = delete_task, font=('Times New Roman', 12))
button1.place(x=180, y=350)

button2 = tk.Button(window, text='track to-do list', bg='white', fg='black', command = show_tracked_tasks, font=('Times New Roman', 12))
button2.place(x=310, y=350)

button3 = tk.Button(window, text='exit', bg='white', fg='black', command = close, font=('Times New Roman', 12))
button3.place(x=400, y=400)

tasks_label = tk.Label(window, text='', bg='purple', fg='white', font=('Times New Roman', 13))
tasks_label.place(x=10, y=300)

window.mainloop()
