import pygame, sys
from pygame.locals import *
from operator import __sub__ as sub

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

    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                for i in range(SQUARE_MAX):
                    if the_squares[i][0].collidepoint(event.pos):
                        if event.button == 1:
                            the_squares[i][1] = 1
                        else:
                            the_squares[i][1] = 2
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            update_squares(DISPLAYSURF, the_squares)
            pygame.display.update()

if __name__ == '__main__':
    main()