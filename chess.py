class Pawn(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy pěšáka.
        Bílý postupuje vpřed (řádek +1), černý zpět (řádek -1).
        """
        row, col = self.position
        moves = []
        if self.color == 'white':
            move = (row + 1, col)
        else:  # black
            move = (row - 1, col)
        
        if self.is_position_on_board(move):
            moves.append(move)
        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy střelce (diagonální pohyby).
        """
        row, col = self.position
        moves = []

        for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for step in range(1, 8):  # může se hýbat až o 7 polí
                move = (row + dr * step, col + dc * step)
                if self.is_position_on_board(move):
                    moves.append(move)
                else:
                    break
        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy věže (vertikální a horizontální pohyby).
        """
        row, col = self.position
        moves = []

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for step in range(1, 8):  # může se hýbat až o 7 polí
                move = (row + dr * step, col + dc * step)
                if self.is_position_on_board(move):
                    moves.append(move)
                else:
                    break
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy královny (kombinace věže a střelce).
        """
        moves = Rook(self.color, self.position).possible_moves() + \
                Bishop(self.color, self.position).possible_moves()
        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy krále (jedno pole všemi směry).
        """
        row, col = self.position
        moves = [
            (row + 1, col), (row - 1, col),
            (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1),
            (row - 1, col + 1), (row - 1, col - 1)
        ]
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    pieces = [
        Pawn("white", (2, 2)),
        Pawn("black", (7, 2)),
        Bishop("white", (4, 4)),
        Rook("black", (1, 1)),
        Queen("white", (3, 3)),
        King("black", (5, 5)),
    ]

    for piece in pieces:
        print(piece)
        print("Possible moves:", piece.possible_moves())
        print()

