import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("470x400")
root.config(bg="#2F4F4F")

user_score = 0
computer_score = 0

def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result = ""
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        user_score += 1
        result = "You win!"
    else:
        computer_score += 1
        result = "Computer wins!"
    
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def on_button_click(user_choice):
    determine_winner(user_choice)

# Title
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 20, "bold"), bg="#2F4F4F", fg="#F5F5F5", relief="ridge", bd=5)
title_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#2F4F4F")
button_frame.pack(pady=20)

button_style = {
    "font": ("Helvetica", 14, "bold"),
    "bg": "#4682B4",
    "fg": "#F5F5F5",
    "width": 10,
    "relief": "raised",
    "bd": 5,
    "cursor": "hand2"
}

rock_button = tk.Button(button_frame, text="Rock", **button_style, command=lambda: on_button_click('rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", **button_style, command=lambda: on_button_click('paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", **button_style, command=lambda: on_button_click('scissors'))
scissors_button.grid(row=0, column=2, padx=10)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#2F4F4F", fg="#F5F5F5", relief="ridge", bd=5)
result_label.pack(pady=20)

# Score Labels
score_frame = tk.Frame(root, bg="#2F4F4F")
score_frame.pack(pady=10)

user_score_label = tk.Label(score_frame, text=f"Your Score: {user_score}", font=("Helvetica", 12, "bold"), bg="#2F4F4F", fg="#F5F5F5")
user_score_label.grid(row=0, column=0, padx=20)

computer_score_label = tk.Label(score_frame, text=f"Computer Score: {computer_score}", font=("Helvetica", 12, "bold"), bg="#2F4F4F", fg="#F5F5F5")
computer_score_label.grid(row=0, column=1, padx=20)

# Reset Button
reset_button = tk.Button(root, text="Reset Scores", font=("Helvetica", 12, "bold"), bg="#D2691E", fg="#F5F5F5", relief="raised", bd=5, cursor="hand2", command=reset_scores)
reset_button.pack(pady=10)

root.mainloop()
