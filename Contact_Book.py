import tkinter as tk
from tkinter import Label
from tkinter import Toplevel

contacts = []

window = tk.Tk()
window.title('Contact Book')
window.geometry('500x500')
window.config(bg='maroon')

def close():
    exit()

def add_contact():
    name = name_entry.get()
    contact = contact_entry.get()
    if name and contact:
        task_list.insert(tk.END, f"{name} : {contact}")
        name_entry.delete(0, tk.END)
        contact_entry.delete(0, tk.END)


def view_contact():
    view_window = Toplevel(window)
    view_window.title('view contact')
    view_window.geometry('400x400')
    view_window.config(bg='maroon')
    
    view_label =tk.Label(view_window, text='Contacts', bg='maroon', fg='white', font=('Times New Roman', 15))
    view_label.pack(pady=10)

    contact_listbox = tk.Listbox(view_window, width=50, height=20)
    contact_listbox.pack(pady=20)

    for contact in task_list.get(0, tk.END):
        contact_listbox.insert(tk.END, contact)


def search_contact():
    search_window = Toplevel(window)
    search_window.title('Search Contact')
    search_window.geometry('400x400')
    search_window.config(bg='maroon')
    
    search_label = tk.Label(search_window, text='search contact', bg='maroon', fg='white', font=('Times New Roman', 15))
    search_label.place(x=150, y=10)
    
    search_entry = tk.Entry(search_window, width=30)
    search_entry.place(x=20, y=80)
    
    result_listbox = tk.Listbox(search_window, width=50, height=14)
    result_listbox.place(x=20, y=130)

    def perform_search():
        query = search_entry.get().lower()
        print(f"Searching for: {query}")
        result_listbox.delete(0, tk.END)
        for contact in task_list.get(0, tk.END):
            print(f"Ckecking contact: {contact}")
            name, contact_number = contact.split(' : ')
            if query in name.lower():
                result_listbox.insert(tk.END, contact)
                print(f"Found match: {contact}")

    search_button = tk.Button(search_window, text='Search', bg='white', fg='black', command=perform_search, font=('Times New Roman', 12))
    search_button.place(x=250, y=80)

    exit_button = tk.Button(search_window, text='close', bg='white', fg='black', command=close,  font=('Times New Roman', 12))
    exit_button.place(x=350, y=350)


def delete_contact():
    selected_contact = task_list.curselection()
    if selected_contact:
        task_list.delete(selected_contact)


label = tk.Label(window, text='CONTACT BOOK', bg='white', fg='black', font=('Times New Roman', 15))
label.place(x=170, y=20)

label = tk.Label(window, text='Name : ', bg='maroon', fg='white',  font=('Times New Roman', 13))
label.place(x=20, y=100)
name_entry = tk.Entry(window, width=30)
name_entry.place(x=140, y=100)

label = tk.Label(window, text='Add Contact : ', bg='maroon', fg='white', font=('Times New Roman', 13))
label.place(x=20, y=150)
contact_entry = tk.Entry(window, width=30)
contact_entry.place(x=140, y=150)

button = tk.Button(window, text='SUBMIT', bg='white', fg='black', command=add_contact, font=('Times New Roman', 10))
button.place(x=400, y=145)

button = tk.Button(window, text=' View Contact', bg='white', fg='black', command=view_contact, font=('Times New Roman', 11))
button.place(x=20, y=230)

task_list = tk.Listbox(width=50, height=14)
task_list.grid(row=1, column=0, columnspan=20, padx=5, pady=15)
task_list.place(x=150, y=220)

button = tk.Button(window, text='Search Contact ', bg='white', fg='black', command=search_contact, font=('Times New Roman', 11))
button.place(x=20, y=320)

button = tk.Button(window, text='Delete Contact ', bg='white', fg='black', command=delete_contact, font=('Times New Roman', 11))
button.place(x=20, y=410)

button = tk.Button(window, text='close ', bg='white', fg='black', command=close, font=('Times New Roman', 10))
button.place(x=450, y=470)

window.mainloop()
