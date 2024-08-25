import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == "Rock" and computer_choice == "Scissors") or \
       (user_choice == "Scissors" and computer_choice == "Paper") or \
       (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    return "You lose!"

# Function to handle the game logic
def play_game(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    # Update scores
    if result == "You win!":
        scores["User"] += 1
    elif result == "You lose!":
        scores["Computer"] += 1

    # Update labels with results
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {scores['User']} | Computer: {scores['Computer']}")
    
# Function to ask user if they want to play again
def play_again():
    response = messagebox.askyesno("Play Again?", "Do you want to play another round?")
    if response:
        user_choice_label.config(text="Your Choice: ")
        computer_choice_label.config(text="Computer's Choice: ")
        result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Initialize scores
scores = {"User": 0, "Computer": 0}

# Create and place widgets
tk.Label(root, text="Choose Rock, Paper, or Scissors:").pack(pady=10)

tk.Button(root, text="Rock", command=lambda: play_game("Rock")).pack(side=tk.LEFT, padx=10)
tk.Button(root, text="Paper", command=lambda: play_game("Paper")).pack(side=tk.LEFT, padx=10)
tk.Button(root, text="Scissors", command=lambda: play_game("Scissors")).pack(side=tk.LEFT, padx=10)

user_choice_label = tk.Label(root, text="Your Choice: ")
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer's Choice: ")
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

score_label = tk.Label(root, text=f"Score - You: {scores['User']} | Computer: {scores['Computer']}")
score_label.pack(pady=5)

play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.pack(pady=10)

# Run the application
root.mainloop()
