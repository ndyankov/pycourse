
import random

def play(board, sign):
    while True:
        empty = []  
        for x in range(3):
            for y in range(3):
                value = board.get(x, y)
                if value == board.EMPTY:
                    empty.append((x, y))

        if empty:
            yield random.choice(empty)
        else:
            break
