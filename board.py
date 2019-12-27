import pieces


class Board:

    board = [[[] for column in range(0, 8)] for row in range(0, 8)]

    def __init__(self):
        for col in range(0, 8):
            board[1][col] = Pawn(1, col, 'black')
            board[6][col] = Pawn(6, col, 'white')

            if col == 0 or col == 7:
                board[0][col] = Rook(0, col, 'black')
                board[7][col] = Rook(7, col, 'white')

            if col == 1 or col == 6:
                board[0][col] = Knight(0, col, 'black')
                board[7][col] = Knight(7, col, 'white')

            if col == 2 or col == 5:
                board[0][col] = Bishop(0, col, 'black')
                board[7][col] = Bishop(7, col, 'white')

            if col == 3:
                board[0][col] == King(0, col, 'black')
                board[7][col] == King(7, col, 'white')

            if col == 4:
                board[0][col] == Queen(0, col, 'black')
                board[7][col] == Queen(7, col, 'white')

    def game_state(self, window):
        for piece in board:
            if piece:
                pygame.window.blit((width, height))
