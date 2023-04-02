import tkinter as tk
import ttkbootstrap as ttk
import random
import pytest
from tic_tac_toe import add_mark, check_win

board_buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0], ]
for row in range(3):
    for column in range(3):
        board_buttons[row][column] = ""

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

def test_add_mark():
    """Test adding a mark
    Return: nothing
    """

    actual_player = "⭕️"
    players = ["❌", "⭕️"]

    actual_player = random.choice(players)
    header_label = f"Player {actual_player} turn"
    add_mark(board_buttons[0], board_buttons[0])
    assert board_buttons[0][0] == actual_player
    assert header_label == "Player ⭕️ turn"


def test_check_win():
    board_buttons[0][0] = "❌"
    board_buttons[0][1] = "❌"
    board_buttons[0][2] = "❌"
    assert check_win() is True

    board_buttons[1][0] = "❌"
    board_buttons[1][1] = "❌"
    board_buttons[1][2] = "❌"
    assert check_win() is True


# Call the main function that is part of pytest so that the
# computer will execute the test functions this file
pytest.main(["-v", "--tb=line", "-rN", __file__])