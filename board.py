from pygame import Surface
from images import board_img, dot
from pieces import *


class Board:

    board = [[[] for y in range(0, 8)] for x in range(0, 8)]

    def __init__(self, window):
        self.board_img = board_img
        self.dot = dot
        for y in range(0, 8):
            self.board[1][y] = Pawn(1, y, 'black')
            self.board[6][y] = Pawn(6, y, 'white')
            if y == 0 or y == 7:
                self.board[0][y] = Rook(0, y, 'black')
                self.board[7][y] = Rook(7, y, 'white')
            if y == 1 or y == 6:
                self.board[0][y] = Knight(0, y, 'black')
                self.board[7][y] = Knight(7, y, 'white')
            if y == 2 or y == 5:
                self.board[0][y] = Bishop(0, y, 'black')
                self.board[7][y] = Bishop(7, y, 'white')
            if y == 3:
                self.board[0][y] == Queen(0, y, 'black')
                self.board[7][y] == Queen(7, y, 'white')
            if y == 4:
                self.board[0][y] == King(0, y, 'black')
                self.board[7][y] == King(7, y, 'white')
        print(self.board)

    selected_x = 0
    selected_y = 0
    # Checks if there is a piece in the coord clicked

    def mouse_clicked(self, mouse_coord):
        self.selected_x = mouse_coord[0]
        self.selected_y = mouse_coord[1]
        if self.board[x][y]:
            list_moves = self.board[self.selected_x][self.selected_y].get_moves()
            legal_moves = legal_moves(list_moves, (x, y))
            return legal_moves
        return None

    def legal_moves(self, list_moves):
        for move in list_moves:
            x = move[0]
            y = move[1]
            if x + self.selected_x is not in range(0, 8):
                list_moves.

    def check_for_check(self, list_moves):
        for move in list_moves:
            x = move[0]
            y = move[1]
            if self.board[x][y]:
                pass

    # Moves a piece from one coord to another
    def move_piece(self, piece_coord, move_coord):
        x1 = piece_coord[0]
        y1 = piece_coord[1]
        x2 = move_coord[0]
        y2 = move_coord[1]
        # If there is a piece in the spot that is selected, the piece is killed
        if self.board[x2][y2]:
            self.board[x2][y2].pop()
        # Updates the new position of the piece in its x and y properties
        self.board[x1][y1].x, self.board[x1][y1].y = x1, y1
        # Switches the pieces from the piece's current to position to the clicked position
        self.board[x1][y1], self.board[x2][y2] = self.board[x2][y2], self.board[x1][y1]

    # Returns the (x, y) coords of all pieces on the board
    def game_state(self):
        piece_coords = []
        for x in range(0, 8):
            for y in range(0, 8):
                if self.board[x][y]:
                    piece_coords.append((x, y))
        return piece_coords
