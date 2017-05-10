import pygame, sys
from pygame.locals import *
from operator import __sub__ as sub

# Square Formatting
SQUARE_LENGTH = 50
SQUARE_MARGIN = 10
# Colours
WHITE = (255,255,255)
BLUE = (80, 80, 183)
YELLOW = (206, 244, 66)

def update_squares(display, the_squares):
    for square in the_squares:
        pygame.draw.rect(display,
                         WHITE,
                         square)

def main():
    pygame.init()
    # Square Details
    the_squares = []
    for i in range(9):
        the_squares = the_squares + [Rect(((i%3)*(SQUARE_LENGTH+SQUARE_MARGIN)+SQUARE_MARGIN,
                                     (i//3)*(SQUARE_LENGTH+SQUARE_MARGIN) +SQUARE_MARGIN,
                                     SQUARE_LENGTH, SQUARE_LENGTH))]

    DISPLAYSURF = pygame.display.set_mode((400,400))
    update_squares(DISPLAYSURF, the_squares)

    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass
                else:
                    pass
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()

if __name__ == '__main__':
    main()