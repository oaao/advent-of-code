"""
EXERCISE PROMPT: http://adventofcode.com/2021/day/6
"""


INPUT = [int(x) for x in open('input', mode='r', encoding='utf-8').read().strip('\n').split(',')]


def spawn(fish_model, days=0):
	model = fish_model[:]
	spawns_waiting = 0
	for i in range(1, days+1):
		model = list(map(lambda x: x-1, model))
		model += [8] * model.count(-1)
		model = [6 if age == -1 else age for age in model]
	return model


# part A solution
print(len(spawn(INPUT, days=80)))

# part B solution
print(len(spawn(INPUT, days=256)))
