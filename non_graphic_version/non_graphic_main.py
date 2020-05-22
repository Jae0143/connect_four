import numpy as np


def create_board():
    # Zero matrics 6 rows by 7 column
    board = np.zeros((6, 7))
    return board


game_over = False
turn = 0

while not game_over:
    # Ask player1 input
    if turn == 0:
        selection_1 = int(input("PLayer1 Make your selection (0-6): "))

    # Ask player2 input
    else:
        selection_1 = int(input("Player2 Make your selection (0-6): "))

    turn += 1

    # divides by 2 -> giving option of 0 and 1
    turn = turn % 2
