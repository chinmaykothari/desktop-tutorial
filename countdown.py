import tkinter as tk
import time
from tkinter import messagebox

root = tk.Tk()
root.title("Count Down Clock ")
root.geometry("600x470+500+70")
root.config(bg="gray12")

hour = tk.StringVar(value="00")
minute = tk.StringVar(value="00")
second = tk.StringVar(value="00")

running = False  # Variable to track countdown status

def reset_timer():
    """Resets the countdown timer to 00:00:00 and stops the timer."""
    global running
    running = False  # Stop the countdown
    hour.set("00")
    minute.set("00")
    second.set("00")

def start_countdown():
    """Starts the countdown timer."""
    global running
    running = True  # Enable countdown
    try:
        total_seconds = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
        countdown(total_seconds)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for hours, minutes, and seconds.")

def countdown(temp):
    """Handles the countdown logic."""
    global running
    if not running:  # Stop countdown if reset is pressed
        return

    if temp >= 0:
        mins, secs = divmod(temp, 60)
        hrs = mins // 60
        mins = mins % 60

        hour.set(f"{hrs:02d}")
        minute.set(f"{mins:02d}")
        second.set(f"{secs:02d}")

        root.after(1000, countdown, temp - 1)
    else:
        messagebox.showinfo("Time Countdown", "Time's up!")
        running = False  # Stop countdown when finished

line_label = tk.Label(root,text="__________________________", font=("times new roman ",30,"bold"),bg="gray12",fg="white")
line_label.place(x=300,y=50,anchor="center")

home_label = tk.Label(root,text ="COUNTDOWN CLOCK", font=("times new roman ",40,"bold"),bg="gray12",fg="white")
home_label.place(x=300,y=30,anchor="center")

line_label = tk.Label(root,text="__________________________", font=("times new roman ",30,"bold"),bg="gray12",fg="white")
line_label.place(x=300,y=150,anchor="center")

reset_btn = tk.Button(root, text="RESET", font=("times new roman ",25,"bold"),width=9,height=1,bg="gray30",fg="white",border=5,command=reset_timer)
reset_btn.place(x=30,y=120,anchor="w")

exit_btn = tk.Button(root, text="EXIT", font=("times new roman ",25,"bold"),width=9,height=1,bg="gray30",fg="white",border=5,command= lambda: root.destroy())
exit_btn.place(x=570,y=120,anchor="e")

line_label = tk.Label(root,text="______________________________________", font=("times new roman ",20,"bold"),bg="gray12",fg="white")
line_label.place(x=300,y=196,anchor="center")

entry_label = tk.Label(root, text="ENTER TIME",font=("times new roman ",30,"bold"),bg="gray12",fg="white")
entry_label.place(x=300,y=210,anchor="center")

copy_label = tk.Label(root, text="Divyanshu Sharma",font=("times new roman ",9,"bold"),bg="gray12",fg="white")
copy_label.place(x=590,y=460,anchor="e")

tk.Entry(root, width=3, font=("times new roman ",30,"bold"), textvariable=hour,border=5).place(x=150, y=260)
tk.Label(root, text=":", font=("times new roman ",30,"bold"),bg="gray12", fg="white").place(x=230, y=260)
tk.Entry(root, width=3, font=("times new roman ",30,"bold"), textvariable=minute,border=5).place(x=260, y=260)
tk.Label(root, text=":", font=("times new roman ",30,"bold"),bg="gray12", fg="white").place(x=340, y=260)
tk.Entry(root, width=3, font=("times new roman ",30,"bold"), textvariable=second,border=5).place(x=370, y=260)

tk.Button(root, text="START TIMER", font=("Times New Roman", 25, "bold"),width=18, bg="gray30", fg="white",border=5 ,command=start_countdown).place(x=300, y=390,anchor="center")

root.mainloop()
