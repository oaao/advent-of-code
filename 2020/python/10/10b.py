

def sublist_at_delimiter(iterable, d):
	
	sublists = []
	group    = []

	for el in iterable:
		if el == d:        # encountered delim
			if group:      # empty groups are just delims as initial, or consecutive
				sublists.append(group)
				group = [] # onward to a new group
		else:
			group.append(el)

	if group:              # last group
		sublists.append(group)

	return sublists


# -------- EXAMINING THE SEQUENCE OF JUMPS (MAKE SURE ADAPTER LIST IS SORTED) --------

INPUT = [int(n.strip('\n'))	for n in open('input', mode='r', encoding='utf-8')]

# here, the initial [0] (outlet) is important, just like 0-indexing
# max(INPUT) + 3 (device) has no effect since it's a monopath / 3hop

nums  = [0] + sorted(INPUT) 
diffs = [b-a for a, b in zip(nums, nums[1:])]

for num, diff in zip(nums, diffs):
	print(f"Joltage {num} - hops to next: {diff}")


# -------- DETERMINE A COMBINATORIAL PATTERN BASED ON DYNAMIC SUBSECTIONS ONLY -------

# If the 3's don't matter, then we just need to abstract the stuff in between into a table of generalised possibilities

pattern = {	# nr consecutive ones : nr of combinations

				# start at a 3hop and stop before the next one
	1 : 1,		#  0 ->  1 ==>                 (0, 1) ==> 1 combination
	2 : 2,		# 42 -> 46 ==> (42, 46), (42, 45, 46) ==> 2 combinations
	3 : 4,		# 29 -> 34 ==> lol u think im actually==> 4 combinations
	4 : 7       #  2 ->  8 ==> gonna write these out  ==> 7 combinations

  # 5 : n/a     in this data pattern, you do not encounter more than a consecutive chain of four 1's
}


# -------------------------- SLAP THAT PATTERN ON YOUR ONES --------------------------


split_out_at_threes  = sublist_at_delimiter(diffs, 3)
num_consecutive_ones = [len(sublist) for sublist in split_out_at_threes]
print(f"\nA count of consecutive ones: \n{num_consecutive_ones}\n")

combinations_instead = [pattern[n] for n in num_consecutive_ones]
print(f"Replacing the counts with their combo counts: \n{combinations_instead}\n")

import functools
combinations = functools.reduce(lambda x, y: x * y, combinations_instead)
print(f"Let's see what we got: {combinations}")
