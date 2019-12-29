from pygame import Surface
from images import board_img, dot
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
                self.board[0][col] == Queen(0, col, 'black')
                self.board[7][col] == Queen(7, col, 'white')
            if col == 4:
                self.board[0][col] == King(0, col, 'black')
                self.board[7][col] == King(7, col, 'white')
        print(self.board)

    def mouse_clicked(self, mouse_coord):
        if self.board[mouse_coord[0]][mouse_coord[1]]:
            return self.board[mouse_coord[0]][mouse_coord[1]].get_moves()
        return None

    def game_state(self, window):
        for row in range(0, 8):
            for col in range(0, 8):
                if self.board[row][col]:
                    window.blit(self.board[row][col].img, (self.board[row]
                                                           [col].y * 120, self.board[row][col].x * 120))
