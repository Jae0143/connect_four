import pygame
import math
import numpy as np

# initalize pygame
pygame.init()

# Row and width count
ROW_COUNT = 6
COL_COUNT = 7

# Set Screen Size
SQUARESIZE = 100
width = SQUARESIZE * COL_COUNT
# giving extra space at the top for displaying the ball
height = SQUARESIZE * (ROW_COUNT + 1)
size = (width, height)

screen = pygame.display.set_mode(size)

# Set title
pygame.display.set_caption("Connect Four")

# font
over_font = pygame.font.Font("ARCADECLASSIC.TTF", 75)


# board drawing
def draw_board(window, board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            # draw rectangle for base of board
            pygame.draw.rect(window, (153, 153, 255),
                             (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            # draw circle
            pygame.draw.circle(window, (0, 255, 128), (
                c * SQUARESIZE + int(SQUARESIZE / 2), r * SQUARESIZE + SQUARESIZE + int(SQUARESIZE / 2)),
                               int(SQUARESIZE / 2 - 6))

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(window, (204, 0, 102), (
                    c * SQUARESIZE + int(SQUARESIZE / 2),
                    height - r * SQUARESIZE - SQUARESIZE + int(SQUARESIZE / 2 - 5)),
                                   int(SQUARESIZE / 2 - 2))
            elif board[r][c] == 2:
                pygame.draw.circle(window, (0, 0, 204), (
                    c * SQUARESIZE + int(SQUARESIZE / 2),
                    height - r * SQUARESIZE - SQUARESIZE + int(SQUARESIZE / 2 - 5)),
                                   int(SQUARESIZE / 2 - 2))
    pygame.display.update()


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
    for c in range(COL_COUNT - (COL_COUNT - 4)):
        for r in range(ROW_COUNT):
            # Check horizontal location
            if board_main[r][c] == player_piece and board_main[r][c + 1] == player_piece and board_main[r][
                c + 2] == player_piece and board_main[r][c + 3] == player_piece:
                return True

    for c in range(COL_COUNT):
        # prevents from going out of index
        for r in range(ROW_COUNT - (ROW_COUNT - 4)):
            # Check vertical
            if board_main[r][c] == player_piece and board_main[r + 1][c] == player_piece and board_main[r + 2][
                c] == player_piece and board_main[r + 3][c] == player_piece:
                return True

    # Positive slope diagonal
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board_main[r][c] == player_piece and board_main[r + 1][c + 1] == player_piece and board_main[r + 2][
                c + 2] == player_piece and board_main[r + 3][c + 3] == player_piece:
                return True
    # Negative slope diagonal
    for c in range(3, COL_COUNT):
        for r in range(ROW_COUNT - 3):
            if board_main[r][c] == player_piece and board_main[r + 1][c - 1] == player_piece and board_main[r + 2][
                c - 2] == player_piece and board_main[r + 3][c - 3] == player_piece:
                return True


game_over = False
turn = 0


def create_board():
    # Zero matrics 6 rows by 7 column
    board_init = np.zeros((ROW_COUNT, COL_COUNT))
    return board_init


board = create_board()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        # Mouse clicking
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, (204, 0, 102), (posx, int(SQUARESIZE / 2)), int(SQUARESIZE / 2 - 2))
            else:
                pygame.draw.circle(screen, (0, 0, 204), (posx, int(SQUARESIZE / 2)), int(SQUARESIZE / 2 - 2))

        if event.type == pygame.MOUSEBUTTONDOWN:
            # reset screen to black
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    # Consequence of winning
                    if winning_move(board, 1):
                        screen.fill((0, 0, 0))
                        winning = over_font.render("Player 1 Wins", 1, (255, 255, 255))
                        screen.blit(winning, (40, 10))
                        game_over = True

            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    # Consequence of winning
                    if winning_move(board, 2):
                        screen.fill((0, 0, 0))
                        winning = over_font.render("Player 2 Wins", 1, (255, 255, 255))
                        screen.blit(winning, (40, 10))
                        game_over = True
            turn += 1
            turn = turn % 2


        draw_board(screen, board)

        if game_over:
            pygame.time.wait(3000)
