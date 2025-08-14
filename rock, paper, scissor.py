import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(background="#596ab6")
root.geometry("500x400")

choices = ["Rock", "Paper", "Scissors"]

# Labels for User and Computer Choices
user_choice_label = tk.Label(root, text="User: ", font=("Segoe UI", 14, "bold"), bg="#9b59b6", fg="white")
computer_choice_label = tk.Label(root, text="Computer: ", font=("Segoe UI", 14, "bold"), bg="#9b59b6", fg="white")
user_choice_label.grid(row=1, column=0, padx=20, pady=20)
computer_choice_label.grid(row=1, column=2, padx=20, pady=20)

# Scores
player_score = tk.Label(root, text="0", font=("Segoe UI", 20, "bold"), bg="#9b59b6", fg="white")
computer_score = tk.Label(root, text="0", font=("Segoe UI", 20, "bold"), bg="#9b59b6", fg="white")
player_score.grid(row=2, column=0)
computer_score.grid(row=2, column=2)

# Message Label
msg = tk.Label(root, font=("Segoe UI", 14, "bold"), bg="#9b59b6", fg="white")
msg.grid(row=3, column=1, pady=20)

# Update Message
def update_message(text, color):
    msg.config(text=text, bg=color, fg="white")

# Update Scores
def update_user_score():
    score = int(player_score["text"])
    player_score.config(text=str(score + 1))

def update_computer_score():
    score = int(computer_score["text"])
    computer_score.config(text=str(score + 1))

# Game Logic
def update_choice(user_choice):
    computer_choice = random.choice(choices)
    user_choice_label.config(text=f"User: {user_choice}")
    computer_choice_label.config(text=f"Computer: {computer_choice}")

    if user_choice == computer_choice:
        update_message("It's a Tie!", "black")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        update_message("You Win!", "green")
        update_user_score()
    else:
        update_message("You Lose!", "red")
        update_computer_score()

# Buttons
rock_btn = tk.Button(root, text="Rock", width=15, height=2, bg="#FF3E4D", fg="white", 
                     font=("Segoe UI", 12, "bold"), command=lambda: update_choice("Rock"))
paper_btn = tk.Button(root, text="Paper", width=15, height=2, bg="#7C7B1F", fg="white",
                      font=("Segoe UI", 12, "bold"), command=lambda: update_choice("Paper"))
scissors_btn = tk.Button(root, text="Scissors", width=15, height=2, bg="#1E0C4B", fg="white",
                         font=("Segoe UI", 12, "bold"), command=lambda: update_choice("Scissors"))

rock_btn.grid(row=4, column=0, pady=10)
paper_btn.grid(row=4, column=1, pady=10)
scissors_btn.grid(row=4, column=2, pady=10)

root.mainloop()
