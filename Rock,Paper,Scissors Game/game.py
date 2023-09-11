import random
import tkinter as tk
from tkinter import messagebox

def play_game():
    player_choice = player_choice_var.get()
    computer_choice = random.choice(choices)
    
    result = determine_winner(player_choice, computer_choice)
    
    messagebox.showinfo("Result", result)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a Tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Paper') or \
         (player_choice == 'Paper' and computer_choice == 'Scissors') or \
         (player_choice == 'Scissors' and computer_choice == 'Rock'):
        return f'Computer wins! {computer_choice} beats {player_choice}'
    else:
        return f'You win! {player_choice} beats {computer_choice}'

choices = ['Rock', 'Paper', 'Scissors']

window = tk.Tk()
window.title("Rock Paper Scissors Game")

player_choice_var = tk.StringVar()

tk.Label(window, text="Choose your move:").pack()
for choice in choices:
    tk.Radiobutton(window, text=choice, variable=player_choice_var, value=choice).pack()

play_button = tk.Button(window, text="Play", command=play_game)
play_button.pack()

window.mainloop()
