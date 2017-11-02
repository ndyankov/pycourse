from board import Board
from players import random1, random2


def contest(player1, player2):
	# initialize board
	board = Board()

	first = Board.X
	second = Board.Z
	p1 = player1(board, first)
	p2 = player2(board, second)

	while not board.game_over():
		board.set(*next(p1), value=first)

		if board.game_over():
			break

		board.set(*next(p2), value=second)

	winner = board.winner()
	print('contest winner is:', winner)
	return winner

def playmany(player1, player2):
	wins = {}
	for x in range(100):
		winner = contest(player1, player2)

		if winner not in wins:
			wins[winner] = 0
		else:
			wins[winner] = wins[winner] + 1

	print(wins)


def main():
	playmany(random2.play, random1.play)


if __name__ == "__main__":
	main()
