"""
EXERCISE PROMPT: http://adventofcode.com/2018/day/9
"""

INPUT = tuple(int(s) for s in open('input.txt').read().split() if s.isdigit())


def play_marble_game(players, marbles):

    circle = [0, ]
    scores = {player: 0 for player in range(players)}

    current_marble_index = 0

    for next_marble in range(1, marbles+1):


        if next_marble % 23 == 0:

            # player keeps their marble and adds its score
            scores[next_marble % players] += next_marble

            # player removes the marble 7ccw and adds its score
            ccw_marble_index = (len(circle) + current_marble_index - 7) % len(circle)
            scores[next_marble % players]  += circle.pop(ccw_marble_index)

            # popping an element at a given index means the element to the right of it gets that index
            current_marble_index = ccw_marble_index

        else:

            next_marble_index = (current_marble_index + 2) % len(circle)

            circle.insert(next_marble_index, next_marble)

            current_marble_index = next_marble_index

    return scores

players, marbles = INPUT

# problem A solution
print(max(play_marble_game(players, marbles).values()))

# problem B solution
#print(max(play_marble_game(players, marbles*100).values()))
