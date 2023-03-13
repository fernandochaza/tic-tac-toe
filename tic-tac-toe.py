import tkinter as tk
from tkinter import ttk
import random


players = ["❌", "⭕️"]
actual_player = random.choice(players)
board_buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


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


def create_dynamic_header():
    """Create a header that will display player's
    turns and game messages
    """
    # Make the header variable accessible for other functions
    global header_label

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

    # Create the board buttons for each row and column
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
    """_summary_

    Args:
        row (_type_): _description_
        column (_type_): _description_
    """
    global actual_player
    player2 = "⭕️" if actual_player == "❌" else "❌"

    if board_buttons[row][column]["text"] == "" and check_win() is False:
        if actual_player == players[0]:
            board_buttons[row][column].configure(foreground="red")
        else:
            board_buttons[row][column].configure(foreground="blue")
        board_buttons[row][column]["text"] = actual_player

        if check_win() is True:
            header_label.configure(text=f"Player {actual_player} WINS!")

        elif check_win() is False and check_empty_spaces_in_board() is True:
            actual_player = player2
            header_label.configure(text=f"Player {actual_player} turn")

        elif check_win() is False and check_empty_spaces_in_board() is False:
            header_label.configure(text="Is a TIE!")


# Define restart_game function
def create_restart_game_button():
    """_summary_"""
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
        command=restart_game,
    )
    restart_game_button.grid()


def restart_game():
    """_summary_"""
    global actual_player
    actual_player = random.choice(players)
    header_label.configure(text=f"Player {actual_player} turn")

    for row in range(3):
        for column in range(3):
            board_buttons[row][column].configure(text="", background="white")


# Define check_win function
def check_win():
    """ """
    for i in range(3):
        if (
            board_buttons[i][0]["text"]
            == board_buttons[i][1]["text"]
            == board_buttons[i][2]["text"]
            != ""
        ):
            board_buttons[i][0].configure(background="green")
            board_buttons[i][1].configure(background="green")
            board_buttons[i][2].configure(background="green")
            return True

        elif (
            board_buttons[0][i]["text"]
            == board_buttons[1][i]["text"]
            == board_buttons[2][i]["text"]
            != ""
        ):
            board_buttons[0][i].configure(background="green")
            board_buttons[1][i].configure(background="green")
            board_buttons[2][i].configure(background="green")
            return True

        elif (
            board_buttons[0][0]["text"]
            == board_buttons[1][1]["text"]
            == board_buttons[2][2]["text"]
            != ""
        ):
            board_buttons[0][0].configure(background="green")
            board_buttons[1][1].configure(background="green")
            board_buttons[2][2].configure(background="green")
            return True

        elif (
            board_buttons[0][2]["text"]
            == board_buttons[1][1]["text"]
            == board_buttons[2][0]["text"]
            != ""
        ):
            board_buttons[0][2].configure(background="green")
            board_buttons[1][1].configure(background="green")
            board_buttons[2][0].configure(background="green")
            return True
    return False


# Define check_empty_spaces_in_board function
def check_empty_spaces_in_board():
    """ """
    spaces = 9

    for row in range(3):
        for column in range(3):
            if board_buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


# Run program with if statement for testing purposes
if __name__ == "__main__":
    main()
