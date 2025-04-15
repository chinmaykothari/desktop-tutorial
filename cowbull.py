import random
import tkinter as tk
from tkinter import messagebox

def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def get_cows_and_bulls(secret, guess):
    bulls = sum(1 for i in range(4) if secret[i] == guess[i])
    cows = sum(1 for digit in guess if digit in secret) - bulls
    return cows, bulls

def check_guess():
    global attempts, secret_number, max_attempts
    guess = entry_guess.get()
    if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4:
        messagebox.showerror("Invalid Input", "Enter 4 unique digits.")
        return
    
    attempts += 1
    cows, bulls = get_cows_and_bulls(secret_number, guess)
    result_label.config(text=f"Cows: {cows}, Bulls: {bulls}, Attempts: {attempts}/{max_attempts}")
    
    if bulls == 4:
        messagebox.showinfo("Congratulations!", f"You guessed the number {secret_number} in {attempts} attempts.")
        root.quit()
    elif attempts >= max_attempts:
        messagebox.showinfo("Game Over", f"You couldn't guess the number {secret_number} within {max_attempts} attempts.")
        root.quit()

def start_game():
    global attempts, secret_number, max_attempts
    secret_number = generate_secret_number()
    max_attempts = int(entry_attempts.get())
    attempts = 0
    result_label.config(text="")
    messagebox.showinfo("Game Started", "Try to guess the 4-digit number!")

root = tk.Tk()
root.title("Cows and Bulls Game")

tk.Label(root, text="Enter the maximum number of attempts:").pack()
entry_attempts = tk.Entry(root)
entry_attempts.pack()

tk.Button(root, text="Start Game", command=start_game).pack()

tk.Label(root, text="Enter your guess:").pack()
entry_guess = tk.Entry(root)
entry_guess.pack()

tk.Button(root, text="Check Guess", command=check_guess).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()