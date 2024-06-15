import tkinter as tk
from tkinter import messagebox, ttk  # Import ttk para usar o Combobox
from logic import TaskLogic
import time

class TaskTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Logger")

        self.logic = TaskLogic()
        task_types = self.logic.get_task_types()

        self.start_time = None
        self.elapsed_time = 0
        self.running = False

        self.task_name = tk.StringVar()
        self.task_type = tk.StringVar()

        tk.Label(root, text="Task Name:").pack()
        tk.Entry(root, textvariable=self.task_name).pack()       
        task_type_combobox = ttk.Combobox(root, textvariable=self.task_type, values=task_types)
        task_type_combobox.pack()

        self.time_label = tk.Label(root, text="Time: 0s")
        self.time_label.pack()

        tk.Button(root, text="Play", command=self.start_timer).pack(side=tk.LEFT)
        tk.Button(root, text="Stop", command=self.stop_timer).pack(side=tk.LEFT)
        tk.Button(root, text="Reset", command=self.reset_timer).pack(side=tk.LEFT)
        tk.Button(root, text="View Log", command=self.view_tasks).pack(side=tk.RIGHT)

    def start_timer(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            self.update_timer()

    def stop_timer(self):
        if self.running:
            self.elapsed_time += int(time.time() - self.start_time)
            self.running = False
            self.save_task()

    def reset_timer(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        self.time_label.config(text="Time: 0s")

    def update_timer(self):
        if self.running:
            current_time = int(time.time() - self.start_time) + self.elapsed_time
            self.time_label.config(text=f"Time: {current_time}s")
            self.root.after(1000, self.update_timer)

    def save_task(self):
        name = self.task_name.get()
        task_type = self.task_type.get()
        duration = self.elapsed_time

        if name and task_type and duration > 0:
            self.logic.save_task(name, task_type, duration)
            messagebox.showinfo("Success", "Task recorded successfully!")
        else:
            messagebox.showwarning("Warning", "Fill in all fields and register a valid duration.")

    def view_tasks(self):
        result_day, result_week, result_month = self.logic.view_tasks()
        self.display_results(result_day, result_week, result_month)

    def display_results(self, result_day, result_week, result_month):
        day_str = "\n".join([f"{task_type}: {duration}s" for task_type, duration in result_day])
        week_str = "\n".join([f"{task_type}: {duration}s" for task_type, duration in result_week])
        month_str = "\n".join([f"{task_type}: {duration}s" for task_type, duration in result_month])

        messagebox.showinfo("Task Log",
                            f"Today:\n{day_str}\n\nLast Week:\n{week_str}\n\nLast Month:\n{month_str}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskTimerApp(root)
    root.mainloop()