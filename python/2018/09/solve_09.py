"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/9
"""

from collections import deque

INPUT = tuple(int(s) for s in open('input.txt').read().split() if s.isdigit())


def play_marble_game(players, marbles):

    circle = deque([0])
    scores = {player: 0 for player in range(players)}

    for next_marble in range(1, marbles+1):

        if next_marble % 23 == 0:

            circle.rotate(7)

            # add score of player's marble and 7ccw marble
            scores[next_marble % players]  += next_marble + circle.pop()

            # popping an element at a given index means the element to the right of it gets that index
            circle.rotate(-1)

        else:

            circle.rotate(-1)
            circle.append(next_marble)

    return scores

players, marbles = INPUT

# problem A solution
print(max(play_marble_game(players, marbles).values()))

# problem B solution
print(max(play_marble_game(players, marbles*100).values()))
