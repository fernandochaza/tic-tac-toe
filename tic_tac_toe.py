import sys
import tkinter as tk
import ttkbootstrap as ttk
import random

main_window = tk.Tk()

players = ["❌", "⭕️"]
actual_player = random.choice(players)
board_buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

winning_possibilities = {
    # Horizontal
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    # Vertical
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    # Diagonal
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
    }


def define_styles():
    styles = ttk.Style()
    styles.configure(
        "TButton",
        font=("Calibri 30 bold"),
        width=5,
        borderwidth="1",
        bordercolor="white",
        focuscolor="",
    )

    styles.configure(
        "win.TButton",
        font=("Calibri 30 bold"),
        width=5,
        borderwidth="1",
        bordercolor="white",
        focuscolor="",
        background="green"
    )


def main():
    # Call the functions that will run the game
    create_main_window()
    define_styles()
    create_dynamic_header()
    create_board()
    create_restart_game_button()

    main_window.mainloop()


def create_main_window():
    main_window.title("Tic Tac Toe")
    main_window.configure(bg="#FFFFFF")

    # Get the project directory and display the window icon
    project_path = sys.argv[0]
    icon_path = project_path.replace("tic_tac_toe.py", "tic-tac-toe.ico")

    # Set a window icon
    try:
        main_window.iconbitmap(icon_path)
    except tk.TclError:
        print(f"Error: could not find icon file '{icon_path}'")

    # Get the screen size to center the window
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    # Set the window size
    window_height = 650
    window_width = 600

    # Get the top-left corner of the window to center it
    left = int(screen_width / 2 - window_width / 2)
    top = int(screen_height / 2 - window_height / 2)

    main_window.geometry(f"{window_width}x{window_height}+{left}+{top}")
    main_window.resizable(False, False)


def create_dynamic_header():
    """Create a header that will display player's
    turns and game messages
    """
    # Make the header variable accessible for other functions
    global header_label

    header_label = ttk.Label(
        main_window,
        text=f"Player {actual_player} turn",
        padding=8,
        font=("Calibri 30 bold"),
        foreground="#000000",
    )
    # Set top/ bottom margins and center it
    header_label.pack(pady=(20, 20), anchor="center")


def create_board():
    board_frame = ttk.Frame()
    board_frame.pack()

    # Create a 3x3 grid with buttons
    for row in range(3):
        for column in range(3):
            board_buttons[row][column] = ttk.Button(
                board_frame,
                padding=("10 35"),
                text="",
                command=lambda row=row, column=column: add_mark(row, column),)
            # Display each button in the grid
            board_buttons[row][column].grid(row=row, column=column,)


def add_mark(row, column):
    """Check if the space is empty and if the game has finished
        before adding the actual player mark to the board.
        Then, check if the player wins to display the winning message
        in the header or change the player turn accordingly

    Args:
        row (int): Board's row to place the mark on.
        column (int): Board's column to place the mark on.
    """
    # Access the actual_player variable
    global actual_player

    # Get the other player's mark value
    player2 = players[1] if actual_player == players[0] else players[0]

    if board_buttons[row][column]["text"] == "" and check_win() is False:
        board_buttons[row][column]["text"] = actual_player

        if check_win() is True:
            header_label.configure(text=f"Player {actual_player} WINS!")

        elif check_empty_spaces_in_board() is True:
            # Change turns
            actual_player = player2
            header_label.configure(text=f"Player {actual_player} turn")

        elif check_win() is False and check_empty_spaces_in_board() is False:
            header_label.configure(text="Is a TIE!")


def create_restart_game_button():
    restart_button_frame = tk.Frame()
    restart_button_frame.pack(pady=50)

    restart_game_button = tk.Button(
        restart_button_frame,
        text="Restart Game",
        font=("Calibri", 24, "bold"),
        background="white",
        foreground="#0062B8",
        command=restart_game,
    )
    restart_game_button.grid()


def restart_game():
    global actual_player
    actual_player = random.choice(players)
    header_label.configure(text=f"Player {actual_player} turn")

    for row in range(3):
        for column in range(3):
            board_buttons[row][column].configure(text="", style="TButton")


def check_win():
    for possibilities in winning_possibilities:
        button1, button2, button3 = possibilities

        if (board_buttons[button1[0]][button1[1]]["text"] ==
            board_buttons[button2[0]][button2[1]]["text"] ==
            board_buttons[button3[0]][button3[1]]["text"] != ""):
            # If true. Change background color of the winning line
            board_buttons[button1[0]][button1[1]].configure(style="win.TButton")
            board_buttons[button2[0]][button2[1]].configure(style="win.TButton")
            board_buttons[button3[0]][button3[1]].configure(style="win.TButton")
            return True
    return False


def check_empty_spaces_in_board():
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
