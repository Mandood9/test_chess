import images


class Piece:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.moves = null
        self.img = null

    def get_moves(self, board):
        moves = []
        for move in self.moves:
            moves.append((self.x+move[0], self.y+move[1]))


class King(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        if color = 'white':
            self.img = w_king
        else:
            self.img = b_king

    def get_moves(self, board):
        super().get_moves(board)


class Queen(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if color = 'white':
            self.img = w_king
        else:
            self.img = b_king

    def get_moves(self, board):
        super().get_moves(board)


class Bishop(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if color = 'white':
            self.img = w_king
        else:
            self.img = b_king

    def get_moves(self, board):
        super().get_moves(board)


class Knight(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if color = 'white':
            self.img = w_king
        else:
            self.img = b_king

    def get_moves(self, board):
        super().get_moves(board)


class Rook(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if color = 'white':
            self.img = w_king
        else:
            self.img = b_king

    def get_moves(self, board):
        super().get_moves(board)


class Pawn(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if color = 'white':
            self.moves = [(0, -1), (-1, -1), (1, -1)]
            self.img = w_king
        else:
            self.moves = [(0, 1), (-1, 1), (1, 1)]
            self.img = b_king

    def get_moves(self, board):
        super().get_moves(board)
