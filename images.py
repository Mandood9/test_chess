import pygame
import os

# White pieces
w_king = pygame.image.load(os.path.join('chess_images', 'Chess_klt60.png'))
w_queen = pygame.image.load(os.path.join('chess_images', 'Chess_qlt60.png'))
w_bishop = pygame.image.load(os.path.join('chess_images', 'Chess_blt60.png'))
w_knight = pygame.image.load(os.path.join('chess_images', 'Chess_nlt60.png'))
w_rook = pygame.image.load(os.path.join('chess_images', 'Chess_rlt60.png'))
w_pawn = pygame.image.load(os.path.join('chess_images', 'Chess_plt60.png'))
# Black pieces
b_king = pygame.image.load(os.path.join('chess_images', 'Chess_kdt60.png'))
b_queen = pygame.image.load(os.path.join('chess_images', 'Chess_qdt60.png'))
b_bishop = pygame.image.load(os.path.join('chess_images', 'Chess_bdt60.png'))
b_knight = pygame.image.load(os.path.join('chess_images', 'Chess_ndt60.png'))
b_rook = pygame.image.load(os.path.join('chess_images', 'Chess_rdt60.png'))
b_pawn = pygame.image.load(os.path.join('chess_images', 'Chess_pdt60.png'))
# board
board_img = pygame.image.load(os.path.join('chess_images', 'chess_board.svg.png'))
