import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

# Initialize the main window
app = ctk.CTk()
app.title("To-Do List")
app.geometry("400x400")

# List to store tasks
tasks = []

# Function to add a task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_task_list()
        entry.delete(0, ctk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to remove a selected task
def remove_task():
    try:
        task = task_list.get(task_list.curselection())
        if task in tasks:
            tasks.remove(task)
            update_task_list()
    except:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to update the task listbox
def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

# UI Elements
frame = ctk.CTkFrame(app)
frame.pack(pady=20)

entry = ctk.CTkEntry(frame, width=300, height=30, placeholder_text="Enter a task")
entry.pack(pady=10)

add_button = ctk.CTkButton(frame, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = ctk.CTkButton(frame, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

task_list = tk.Listbox(app, width=50, height=20)
task_list.pack(pady=20)

# Start the main event loop
app.mainloop()
