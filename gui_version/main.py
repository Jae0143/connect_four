import pygame

# initalize pygame
pygame.init()

# Row and width count
ROW_COUNT = 6
COL_COUNT = 7

# Set Screen Size
SQUARESIZE = 100
width = SQUARESIZE * COL_COUNT
# giving extra space at the top for displaying the ball
height = (SQUARESIZE + 1) * ROW_COUNT
size = (width, height)

screen = pygame.display.set_mode(size)

# Set title
pygame.display.set_caption("Connect Four")


# board drawing
def draw_board(window):
    pass


game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        # Mouse clicking
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass