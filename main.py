import pygame
import sys
from pygame.locals import *
from board import Board

pygame.init()

window = pygame.display.set_mode((960, 960))
pygame.display.set_caption("Chess Game")
clock = pygame.time.Clock()

b = Board(window)


def redraw_game_window():
    window.blit(b.board_img, (0, 0))
    piece_coords = b.game_state()
    for piece_coord in piece_coords:
        x = piece_coord[0]
        y = piece_coord[1]
        window.blit(self.board[x][y].img, coord_scale((self.board[x]
                                                       [y].y, self.board[x][y].x), False))
    pygame.display.update()


def coord_scale(coords, down=True):
    if down:
        x = coords[1] // 120
        y = coords[0] // 120
    else:
        x = coords[1] * 120
        y = coords[0] * 120
    return (x, y)


while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Detects the first click
        if event.type == MOUSEBUTTONDOWN:
            mouse_coord_inital = coord_scale(pygame.mouse.get_pos())

            # Checks if the click gave back some moves at the position of the mouse click
            if (list_moves: = b.mouse_clicked(mouse_coord_inital)) != None:
                # Blits dots for available moves
                for move in list_moves:
                    window.blit(b.dot, coord_scale(move, False))
                # Waits for the second click
                while clicked:
                    = True:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == MOUSEBUTTONDOWN:

                            # Checks if the second click was is the list of available moves
                            if (mouse_coord_second: = coord_scale(pygame.mouse.get_pos())) is in list_moves:
                                b.move_piece(mouse_coord_inital, mouse_coord_second)
                            # Exits the second click loop
                            clicked = False

    redraw_game_window()
