import numpy as np

# global and constant
ROW_COUNT = 6
COL_COUNT = 7

# Draw board
def create_board():
    # Zero matrics 6 rows by 7 column
    board = np.zeros((6, 7))
    return board


def drop_piece():
    pass


# Check if player input is valid
def is_valid_location(board, column):
    pass


# Check for open row
def get_next_open_row(board, column):
    for row_num in range(ROW_COUNT):
        if board[row_num][col]:
            return row_num




game_over = False
turn = 0

while not game_over:
    print(create_board())
    # Ask player1 input
    if turn == 0:
        col_select_1 = int(input("PLayer1 Make your selection (0-6): "))

    # Ask player2 input
    else:
        col_select_2 = int(input("Player2 Make your selection (0-6): "))

    turn += 1

    # divides by 2 -> giving option of 0 and 1
    turn = turn % 2
