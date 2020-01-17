from images import *

# Arrange moves so there is only one direction for each list


class Piece:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return self.__class__.__name__

    def sort_moves(self):
        sorted_moves = []
        for move in self.moves:

    def get_moves(self, board):
        moves = []
        for move in self.moves:
            if self.x + move[0] is in range(8) and self.y + move[1] is in range(8):
                moves.append((self.x + move[0], self.y + move[1]))
        return moves


class King(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        if color == 'white':
            self.img = w_king
        else:
            self.img = b_king

    def get_moves(self, board):
        super().get_moves(board)


class Queen(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.unit_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]
        self.moves = []
        for move in self.unit_moves:
            moves_in_one_dir = []
            if move[0] != 0 and move[1] != 0:
                for constant in range(1, 9):
                    change = (move[0] * constant, move[1] * constant)
                    moves_in_one_dir.append(change)
            else:
                if move[0] != 0:
                    for constant in range(1, 9):
                        change = (move[0] * constant, 0)
                        moves_in_one_dir.append(change)
                else:
                    for constant in range(1, 9):
                        change = (0, move[1] * constant)
                        moves_in_one_dir.append(change)
            self.moves.append(moves_in_one_dir)
        if color == 'white':
            self.img = w_queen
        else:
            self.img = b_queen

    def get_moves(self, board):
        super().get_moves(board)


class Bishop(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.unit_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        self.moves = []
        # Puts the moves in a list so one direction takes one list inside the list of moves
        for move in self.unit_moves:
            moves_in_one_dir = []
            for constant in range(1, 9):
                change = (move[0] * constant, move[1] * constant)
                moves_in_one_dir.append(change)
            self.moves.append(moves_in_one_dir)
        if color == 'white':
            self.img = w_bishop
        else:
            self.img = b_bishop

    def get_moves(self, board):
        super().get_moves(board)


class Knight(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

        if color == 'white':
            self.img = w_knight
        else:
            self.img = b_knight

    def get_moves(self, board):
        super().get_moves(board)


class Rook(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.unit_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.moves = []
        # Puts the moves in a list so one direction takes one list inside the list of moves
        for move in self.unit_moves:
            moves_in_one_dir = []
            if move[0] != 0:
                for constant in range(1, 9):
                    change = (move[0] * constant, 0)
                    moves_in_one_dir.append(change)
            else:
                for constant in range(1, 9):
                    change = (0, move[1] * constant)
                    moves_in_one_dir.append(change)
            self.moves.append(moves_in_one_dir)
        if color == 'white':
            self.img = w_rook
        else:
            self.img = b_rook

    def get_moves(self, board):
        super().get_moves(board)


class Pawn(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if color == 'white':
            self.moves = [(0, -1), (-1, -1), (1, -1), (0, -2)]
            self.img = w_pawn
        else:
            self.moves = [(0, 1), (-1, 1), (1, 1), (0, 2)]
            self.img = b_pawn

    def get_moves(self, board):
        super().get_moves(board)
