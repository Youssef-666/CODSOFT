import tkinter as tk
from tkinter import messagebox
import random

def play_game(user_choice):
    global user_score, pc_score

    pc_choice = random.choice(options)

    if user_choice == pc_choice:
        result = "TIE"
    elif (user_choice == 'R' and pc_choice == 'S') or (user_choice == 'S' and pc_choice == 'P') or (user_choice =='P' and pc_choice == 'R'):
        user_score += 1
        result = "WIN"
    else:
        pc_score += 1
        result = "LOSE"

    result_label.config(text=f"Your choice: {user_choice}, Computer choice: {pc_choice}. It's a {result}")
    score_label.config(text=f"Your score = {user_score}, Computer score = {pc_score}.")

    if messagebox.askyesno("Play Another Round?", "Do you want to play another round?"):
        reset_labels()
    else:
        end_game()

def reset_labels():
    result_label.config(text="")
    score_label.config(text="")

def end_game():
    if user_score == pc_score:
        messagebox.showinfo("Game Over", "IT'S A TIE!")
    elif user_score > pc_score:
        messagebox.showinfo("Game Over", "WINNER!")
    else:
        messagebox.showinfo("Game Over", "Game Over!")
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Initialize options and scores
options = ['R', 'P', 'S']
user_score = pc_score = 0

# Create and configure GUI elements
user_label = tk.Label(root, text="Choose: R for Rock, P for Paper, S for Scissors")
user_label.pack()

rock_button = tk.Button(root, text="Rock", command=lambda: play_game('R'))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_game('P'))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game('S'))
scissors_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

score_label = tk.Label(root, text="")
score_label.pack()


# Start the Tkinter event loop
root.mainloop()
