"""
EXERCISE PROMPT: http://adventofcode.com/2020/day/16
"""
from functools import reduce


def parse_input(filename='input'):
	"""Parse input file into operable terms."""

	with open(filename, mode='r', encoding='utf-8') as f:
		lines = tuple(l.strip('\n') for l in f)

	endpts   = (0,) + tuple(n for i, ln in enumerate(lines) for n in (i, i+2) if ln == '') + (len(lines),)
	sections = (
		lines[i:j] for i, j in zip(endpts, endpts[1:])
	)

	rules, _, (ticket,), _, nearby_tickets = sections

	ticket         = tuple(int(s) for s in ticket.split(','))
	nearby_tickets = tuple(
		(i, tuple(int(s) for s in ln.split(',')))
		for i, ln in enumerate(nearby_tickets)
	)

	return rules, ticket, nearby_tickets


def parse_rules(rules):
	"""Parse rules strings into a ruleset dictionary."""
	ruleset = {}

	for rule in rules:
		s  = rule.replace(': ', ',').replace('-', ',').replace(' or ', ',').replace(' ', '_')
		ln = s.split(',')
		key, min1, max1, min2, max2 = ln

		ruleset[key] = (int(min1), int(max1)), (int(min2), int(max2))

	return ruleset


def get_invalid_tickets_and_values(ranges, tickets):
	"""Get an enumerated list of bad tickets and invalid values within each."""

	bad_tickets = []

	for i, ticket in tickets:

		bad_values = tuple(n for n in ticket if not any(lower <= n <= upper for lower, upper in ranges))

		if bad_values:
			bad_tickets.append(
				(i, ticket, bad_values)
			)

	return bad_tickets


def get_valid_tickets(tickets, rules):
	"""Get a filtered list of only tickets with no invalid values."""

	ranges = tuple(tp for vals in parse_rules(rules).values() for tp in vals)

	return tuple(
		ticket for i, ticket in tickets
		if i not in {i for i, _, _ in get_invalid_tickets_and_values(ranges, tickets)}
	)


def match_possible_ticket_rows(tickets, rules):
	"""Determine which ticket columns *can* match which fields."""

	tickets = get_valid_tickets(tickets, rules)
	ruleset = parse_rules(rules)

	inverse = zip(*tickets)
	matches = {field: [] for field in ruleset}

	for i, column in enumerate(inverse):
		for field in ruleset:
			if all(
				any(lower <= n <= upper for lower, upper in ruleset[field])
				for n in column
			):
				matches[field].append(i)

	return matches


def match_exact_ticket_rows(tickets, rules):
	"""Reduce possible matches into exact matches."""

	possible = match_possible_ticket_rows(tickets, rules)
	exact    = {}

	while possible:
		# sort by matches list length so we can a) both work in sequence, and
		# b) run off a generator while exhausting the possible dict itself
		for k, v in sorted(possible.items(), key=lambda d: len(d[1])):
			if len(v) == 1:
				n, = possible.pop(k, None)
				exact[k] = n
				for _, values in possible.items():
					values.remove(n)

	return exact


RULES, TICKET, NEARBY_TICKETS = parse_input()

# part A solution
ranges = tuple(tp for vals in parse_rules(RULES).values() for tp in vals)
print(
	sum(
		n
		for i, _, vals in get_invalid_tickets_and_values(ranges, NEARBY_TICKETS)
		for n in vals
	)
)

# part B solution
from functools import reduce
print(
	reduce(
		lambda x, y: x * y,
		{
			TICKET[i]
			for field, i in match_exact_ticket_rows(NEARBY_TICKETS, RULES).items()
			if field.startswith('departure')
		}
	)
)
