"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/4
"""


DRAW_SEQ, *BOARDS = [s.strip('\n') for s in open('input', mode='r', encoding='utf-8')]

draw_seq  = list(map(int, DRAW_SEQ.split(',')))
boards = tuple(
	tuple(
		tuple(
			map(
				int,
				filter(
					lambda el: el != '', 
					row.split(' '))
				)
			)
		for row in board
	)
	for board in (BOARDS[i:i+5] for i in range(1, len(BOARDS), 6))
)


def get_draws_and_winner(draw_seq, boards):
	drawn = draw_seq[:4]
	for _ in range(len(draw_seq[4:])):
		drawn.append(draw_seq.pop(4))
		for board in boards:
			if any((
				any(all(n in drawn for n in row) for row in board),
				any(all(n in drawn for n in col) for col in zip(*board)),
			)):
				return drawn, board


def calc_winner_score(draws, board):
	return draws[-1] * sum(filter(lambda n: n not in draws, (n for row in board for n in row)))


# part A solution
print(calc_winner_score(*get_draws_and_winner(draw_seq, boards)))
