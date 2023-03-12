import tkinter as tk
from tkinter import ttk
import random


# Declare/Initialize global variables needed
player1 = "❌"
player2 = "⭕️"

board_buttons = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

# Create a new style object to use ttk styling
style = ttk.Style()


# Define main function
def main():
    
    main_window = tk.Tk()
    main_window.title("Tic Tac Toe")
    main_window.geometry("700x700")
    
    
    main_window.mainloop()


# Define create_board function
def create_dinamic_header(main_window):
    header_label = tk.Label(
        text = f"Player {player1} turn",
        padding=8,
        font=("Calibri", 30, "bold"), 
        foreground="#0062B8")



# Define restart_game function
def restart_game():
    pass


# Define check_win function
def check_win():
    pass


# Define check_tie function
def check_tie():
    pass


# Define check_empty_spaces_in_board function
def check_empty_spaces_in_board():
    pass


# Run program with if statement for testing purposes
if __name__ == "__main__":
    main()