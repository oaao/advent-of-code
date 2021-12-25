"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/6
"""


INPUT = [int(x) for x in open('input', mode='r', encoding='utf-8').read().strip('\n').split(',')]


def spawn(initial_state, days=0):
	# use a register of 0-8 (possible age states)
	spawn_state = [0] * 9
	# initialise spawn state with starting fish ages
	for unique_age in set(initial_state):
		spawn_state[unique_age] = initial_state.count(unique_age)
	for i in range(1, days):
		# just rotate the fuckers around by day
		spawn_state = spawn_state[1:] + spawn_state[:1]
		# and reset 0-day fish back to 6-day
		spawn_state[7] += spawn_state[0]

	return spawn_state



# part A solution
print(sum(spawn(INPUT, days=80)))

# part B solution
print(sum(spawn(INPUT, days=256)))
