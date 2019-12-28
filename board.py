from pygame import Surface
from images import board_img
from pieces import *


class Board:

    board = [[[] for column in range(0, 8)] for row in range(0, 8)]

    def __init__(self, window):
        window.blit(board_img, (0, 0))
        for col in range(0, 8):
            self.board[1][col] = Pawn(1, col, 'black')
            self.board[6][col] = Pawn(6, col, 'white')

            if col == 0 or col == 7:
                self.board[0][col] = Rook(0, col, 'black')
                self.board[7][col] = Rook(7, col, 'white')

            if col == 1 or col == 6:
                self.board[0][col] = Knight(0, col, 'black')
                self.board[7][col] = Knight(7, col, 'white')

            if col == 2 or col == 5:
                self.board[0][col] = Bishop(0, col, 'black')
                self.board[7][col] = Bishop(7, col, 'white')

            if col == 3:
                self.board[0][col] == King(0, col, 'black')
                self.board[7][col] == King(7, col, 'white')

            if col == 4:
                self.board[0][col] == Queen(0, col, 'black')
                self.board[7][col] == Queen(7, col, 'white')

    def game_state(self, window):
        for piece in self.board:
            if piece:
                pygame.window.blit((width, height))
