import pygame, sys
from pygame.locals import *

# Square Formatting
SQUARE_LENGTH = 50
SQUARE_MARGIN = 10
SQUARE_MAX = 9
# Colours
WHITE = (255,255,255)
BLUE = (80, 80, 183)
YELLOW = (206, 244, 66)

def update_squares(display, the_squares):
    for square in the_squares:
        if square[1] == 1:
            colour = YELLOW
        elif square[1] == 2:
            colour = BLUE
        else:
            colour = WHITE
        pygame.draw.rect(display,
                         colour,
                         square[0])

def check_win(the_squares):
    the_squares = [square[1] for square in the_squares]
    winner = None
    # Horizontal Checks
    for x in [1,4,7]:
        if the_squares[x] is not 0 and \
                        the_squares[x-1] == the_squares[x] and the_squares[x] == the_squares[x+1]:
            winner = the_squares[x]
    # Vertical Checks
    for x in [3,4,5]:
        if the_squares[x] is not 0 and \
                        the_squares[x-3] == the_squares[x] and the_squares[x] == the_squares[x+3]:
            winner = the_squares[x]
    # Diagonal Checks
    if the_squares[4] is not 0:
        if the_squares[0] == the_squares[4] and the_squares[4] == the_squares[8]:
            winner =  the_squares[4]
        if the_squares[2] == the_squares[4] and the_squares[4] == the_squares[6]:
            winner =  the_squares[4]
    return winner

def main():
    pygame.init()
    # Square Details
    the_squares = []
    for i in range(SQUARE_MAX):
        the_squares = the_squares + [Rect(((i%3)*(SQUARE_LENGTH+SQUARE_MARGIN)+SQUARE_MARGIN,
                                     (i//3)*(SQUARE_LENGTH+SQUARE_MARGIN) +SQUARE_MARGIN,
                                     SQUARE_LENGTH, SQUARE_LENGTH))]
    the_squares = [[x] + [y] for x, y in zip(the_squares, [0 for _ in range(9)])]

    DISPLAYSURF = pygame.display.set_mode((400,400))
    update_squares(DISPLAYSURF, the_squares)
    player = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                for i in range(SQUARE_MAX):
                    if the_squares[i][0].collidepoint(event.pos):
                        if player == 0:
                            the_squares[i][1] = 1
                        else:
                            the_squares[i][1] = 2
                        player = 0 if player == 1 else 1
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            update_squares(DISPLAYSURF, the_squares)
            pygame.display.update()
            winner = check_win(the_squares)
            if winner:
                print("Player {0} wins.".format(winner))
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
