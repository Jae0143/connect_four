import numpy as np

# global and constant
ROW_COUNT = 6
COL_COUNT = 7


# Draw board
def create_board():
    # Zero matrics 6 rows by 7 column
    board = np.zeros((6, 7))
    return board


# dropping piece into the game
def drop_piece(board, row, column, player_piece):
    board[row][column] = player_piece


# Check if player input is valid
def is_valid_location(board, column):
    return board[5][column] == 0


# Check for open row
def get_next_open_row(board, column):
    for row_num in range(ROW_COUNT):
        if board[row_num][column] == 0:
            return row_num


# flip the board so the top row goes to the bottom
def print_board(board):
    # flip board over 0th row
    return np.flip(board, 0)


game_over = False
turn = 0

board = create_board()

while not game_over:
    # Ask player1 input
    if turn == 0:
        col_select_1 = int(input("PLayer1 Make your selection (0-6): "))
        if is_valid_location(board, col_select_1):
            row = get_next_open_row(board, col_select_1)
            drop_piece(board, row, col_select_1, 1)

    # Ask player2 input
    else:
        col_select_2 = int(input("Player2 Make your selection (0-6): "))
        if is_valid_location(board, col_select_2):
            row = get_next_open_row(board, col_select_2)
            drop_piece(board, row, col_select_2, 2)

    turn += 1

    # divides by 2 -> giving option of 0 and 1
    turn = turn % 2

    print(print_board(board))
