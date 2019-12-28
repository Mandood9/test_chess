import pygame
import sys
from pygame.locals import *
from board import Board

pygame.init()

window = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption("Chess Game")

b = Board(window)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mouse_coord = pygame.mouse.get_pos()
            print(mouse_coord)
    pygame.display.update()
