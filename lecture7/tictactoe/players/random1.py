
def play(board, sign):
    for x in range(3):
        for y in range(3):
            value = board.get(x, y)
            if value == board.EMPTY:
                yield (x, y)