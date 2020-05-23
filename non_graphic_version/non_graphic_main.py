import numpy as np

# global and constant
ROW_COUNT = 6
COL_COUNT = 7


# Draw board
def create_board():
    # Zero matrics 6 rows by 7 column
    board_init = np.zeros((ROW_COUNT, COL_COUNT))
    return board_init


# dropping piece into the game
def drop_piece(board_main, rows, column, player_piece):
    board_main[rows][column] = player_piece


# Check if player input is valid
def is_valid_location(board_main, column):
    return board_main[ROW_COUNT - 1][column] == 0


# Check for open row
def get_next_open_row(board_main, column):
    for row_num in range(ROW_COUNT):
        if board_main[row_num][column] == 0:
            return row_num


# flip the board so the top row goes to the bottom
def print_board(board_main):
    # flip board over 0th row
    return np.flip(board_main, 0)


# Check for winning move
def winning_move(board_main, player_piece):
    for c in range(COL_COUNT-(COL_COUNT - 4)):
        for r in range(ROW_COUNT):
            # Check horizontal location
            if board_main[r][c] == player_piece and board_main[r][c + 1] == player_piece and board_main[r][c + 2] == player_piece and board_main[r][c + 3] == player_piece:
                return True

    for c in range(COL_COUNT):
        # prevents from going out of index
        for r in range(ROW_COUNT-(ROW_COUNT - 4)):
            # Check vertical
            if board_main[r][c] == player_piece and board_main[r + 1][c] == player_piece and board_main[r + 2][
                c] == player_piece and board_main[r + 3][c] == player_piece:
                return True

    # Positive slope diagonal
    for c in range (COL_COUNT - 3):
        for r in range(ROW_COUNT -3):
            if board_main[r][c] == player_piece and board_main[r + 1][c + 1] == player_piece and board_main[r + 2][c + 2] == player_piece and board_main[r + 3][c + 3] == player_piece:
                return True
    # Negative slope diagonal
    for c in range(3, COL_COUNT):
        for r in range(ROW_COUNT - 3):
            if board_main[r][c] == player_piece and board_main[r + 1][c - 1] == player_piece and board_main[r + 2][c - 2] == player_piece and board_main[r + 3][c - 3] == player_piece:
                return True



game_over = False
turn = 0

board = create_board()

while not game_over:
    # Ask player1 input
    if turn == 0:
        col_select_1 = int(input("PLayer1 Make your selection (0-{}): ".format(COL_COUNT - 1)))
        if is_valid_location(board, col_select_1):
            row = get_next_open_row(board, col_select_1)
            drop_piece(board, row, col_select_1, 1)
            # Consequence of winning
            if winning_move(board, 1):
                print("Player 1 wins ")
                game_over = True

    # Ask player2 input
    else:
        col_select_2 = int(input("Player2 Make your selection (0-{}): ".format(COL_COUNT - 1)))
        if is_valid_location(board, col_select_2):
            row = get_next_open_row(board, col_select_2)
            drop_piece(board, row, col_select_2, 2)
            # Consequence of winning
            if winning_move(board, 2):
                print("Player 2 wins ")
                game_over = True

    turn += 1

    # divides by 2 -> giving option of 0 and 1
    turn = turn % 2

    print(print_board(board))
