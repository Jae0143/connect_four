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
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            # draw rectangle for base of board
            pygame.draw.rect(window, (153, 153, 255),
                             (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            # draw circle
            pygame.draw.circle(window, (0, 255, 128), (
            c * SQUARESIZE + int(SQUARESIZE / 2), r * SQUARESIZE + SQUARESIZE + int(SQUARESIZE / 2)),
                               int(SQUARESIZE / 2 - 6))


game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        # Mouse clicking
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    draw_board(screen)
    pygame.display.update()
