"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/4
"""

import operator


DRAW_SEQ, *BOARDS = [s.strip('\n') for s in open('input', mode='r', encoding='utf-8')]

draw_seq = list(map(int, DRAW_SEQ.split(',')))
boards   = list(
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


def get_draws_and_winners(draw_seq, boards, first_winner=False):
	draw_pos = 0
	boards = boards[:]
	winners = []
	while boards:
		for board in boards:
			if any((
				any(all(n in draw_seq[:draw_pos+1] for n in row) for row in board),
				any(all(n in draw_seq[:draw_pos+1] for n in col) for col in zip(*board)),
			)):
				if first_winner:
					return draw_pos, board
				else:
					winners.append((draw_pos, board))
					boards.remove(board)
		draw_pos += 1
	return winners


def calc_winner_score(draw_seq, draw_pos, board):
	return operator.mul(
		draw_seq[draw_pos],
		sum(
			filter(
				lambda n: n not in draw_seq[:draw_pos+1],
				(n for row in board for n in row)
			)
		)
	)


# part A solution
print(
	calc_winner_score(
		draw_seq,
		*get_draws_and_winners(draw_seq, boards, first_winner=True)
	)
)

# part B solution
print(
	calc_winner_score(
		draw_seq,
		*get_draws_and_winners(draw_seq, boards)[-1]
	)
)