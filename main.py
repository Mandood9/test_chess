import pygame
import sys
from pygame.locals import *
from board import Board

pygame.init()

window = pygame.display.set_mode((960, 960))
pygame.display.set_caption("Chess Game")

b = Board(window)


def redraw_game_window():
    piece_coords = b.game_state(window)
    window.blit(self.board[row][col].img, (self.board[row]
                                           [col].y * 120, self.board[row][col].x * 120))
    pygame.display.update()


def coord_scale(coords):
    x = coords[1] // 120
    y = coords[0] // 120
    return (x, y)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mouse_coord = coord_scale(pygame.mouse.get_pos())
            print(mouse_coord)
            list_moves = b.mouse_clicked(mouse_coord)

    redraw_game_window()
