import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    description = task_entry.get()
    if description:
        tasks.append({"description": description, "completed": False})
        task_entry.delete(0, tk.END)
        refresh_tasks()
    else:
        messagebox.showwarning("Input Error", "Task description cannot be empty")

def refresh_tasks():
    for widget in tasks_frame.winfo_children():
        widget.destroy()
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        task_label = tk.Label(tasks_frame, text=f"{idx}. {task['description']} - {status}")
        task_label.pack()

def mark_task_complete():
    try:
        task_id = int(task_entry.get()) - 1
        tasks[task_id]["completed"] = True
        refresh_tasks()
    except (ValueError, IndexError):
        messagebox.showwarning("Task Error", "Invalid task ID")

def delete_task():
    try:
        task_id = int(task_entry.get()) - 1
        del tasks[task_id]
        refresh_tasks()
    except (ValueError, IndexError):
        messagebox.showwarning("Task Error", "Invalid task ID")

root = tk.Tk()
root.title("To-Do List")

input_frame = tk.Frame(root)
input_frame.pack()

tasks_frame = tk.Frame(root)
tasks_frame.pack()

task_entry = tk.Entry(input_frame, width=40)
task_entry.grid(row=0, column=0, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5)

complete_button = tk.Button(input_frame, text="Mark Complete", command=mark_task_complete)
complete_button.grid(row=0, column=2, padx=5, pady=5)

delete_button = tk.Button(input_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=3, padx=5, pady=5)

root.mainloop()
