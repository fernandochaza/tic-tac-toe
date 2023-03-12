import tkinter as tk
from tkinter import ttk
import random


# Declare/Initialize global variables needed
players = ["❌", "⭕️"]

actual_player = random.choice(players)

board_buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# Define main function
def main():
    main_window = tk.Tk()
    main_window.title("Tic Tac Toe")
    main_window.geometry("700x700")
    main_window.configure(bg="#0062B8")
    main_window.resizable(False, False)

    create_dynamic_header()
    create_board()
    create_restart_game_button()

    main_window.mainloop()


# Define create_board function
def create_dynamic_header():
    header_label = ttk.Label(
        text=f"Player {actual_player} turn",
        padding=8,
        font=("Calibri", 30, "bold"),
        foreground="#0062B8",
    )

    # Set top and bottom margins of header and center it
    header_label.pack(pady=(10, 20), anchor="center")


def create_board():
    board_frame = tk.Frame()
    board_frame.pack()

    for row in range(3):
        for column in range(3):
            board_buttons[row][column] = tk.Button(
                board_frame,
                text="",
                background="white",
                font=("Calibri", 30, "bold"),
                width=5,
                height=2,
                command=lambda row=row, column=column: add_mark(row, column),
            )
            # Create the board buttons for each row/column combination
            board_buttons[row][column].grid(row=row, column=column)


def add_mark(row, column):
    board_buttons[row][column]["text"] = actual_player


# Define restart_game function
def create_restart_game_button():
    style = ttk.Style()
    style.configure(
        "restart_game_button.TButton",
        font=("Calibri", 24, "bold"),
        padding=5,
        background="white",
        foreground="#0062B8",
        relief="raised",
    )

    restart_button_frame = tk.Frame()
    restart_button_frame.pack(pady=50)

    restart_game_button = ttk.Button(
        restart_button_frame,
        style="restart_game_button.TButton",
        text="Restart Game",
        command=restart_game(),
    )

    restart_game_button.grid()


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
