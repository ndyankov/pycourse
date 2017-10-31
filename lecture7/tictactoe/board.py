
"""
Tic-tac-toe board.
"""

def printer(funcset):
    """A print decorator for Board.set method"""
    def wrapper(instance, x, y, value):
        res = funcset(instance, x, y, value)
        print("{} played on ({}, {})".format(value.upper(), x, y))
        print(instance)
        if instance.game_over():
            winner = instance.winner()
            if winner is not None:
                print("{} wins".format(winner.upper()))
            else:
                print("no one wins")

        return res

    return wrapper


class Board(object):
    X = 'x' # x
    Z = 'o' # zero
    EMPTY = ' '

    LINES = (
        # horizontal
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),

        # vertical
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),

        # diagonal
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
    )

    def __init__(self):

        self.board = [
            [Board.EMPTY, Board.EMPTY, Board.EMPTY],
            [Board.EMPTY, Board.EMPTY, Board.EMPTY],
            [Board.EMPTY, Board.EMPTY, Board.EMPTY]
        ]

        self.last_played = Board.EMPTY

    def validate(self, x, y):
        if x not in range(3):
            raise ValueError('outside board')
        if y not in range(3):
            raise ValueError('outside board')

    def get(self, x, y):
        self.validate(x, y)
        return self.board[x][y]

    @printer
    def set(self, x, y, value):
        self.validate(x, y)
        if value not in (Board.X, Board.Z):
            raise ValueError('value not allowed')

        current = self.board[x][y]
        if current != Board.EMPTY:
            raise ValueError('cell is not empty')

        if self.last_played != Board.EMPTY:
            if self.last_played == value:
                raise ValueError('cheating!')

        self.last_played = value
        self.board[x][y] = value

    def game_over(self):
        """Determine if game is over"""
        return (self.winner() is not None) or not self.has_empty()

    def winner(self):
        """Get winner"""
        for line in Board.LINES:
            values = set(self.get(x, y) for (x, y) in line)
            if len(values) == 1 and Board.EMPTY not in values:
                return list(values)[0]
        return None

    def has_empty(self):
        for line in Board.LINES:
            for x, y in line:
                if self.get(x, y) == Board.EMPTY:
                    return True
        return False

    def __str__(self):
        rows = []
        for x in range(3):
            column = []
            column.append('')
            for y in range(3):
                column.append(self.board[x][y])
            column.append('')
            rows.append('|'.join(column))
        return '\n'.join(rows)

def main():
    board = Board()
    board.set(0, 0, Board.X)
    board.set(1, 1, Board.Z)
    board.set(0, 1, Board.X)
    board.set(2, 2, Board.Z)
    board.set(0, 2, Board.X)


if __name__ == "__main__":
    main()
