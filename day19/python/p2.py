text_file = open("input-p1-test.txt", "r")
input = text_file.read()
text_file.close()

parts = input.split('\n\n')

raw_workflows = parts[0].splitlines()
raw_ratings = parts[1].splitlines()
workflows = {}

for wf in raw_workflows:
	parts = wf.split('{')
	name = parts[0]
	raw_rules = parts[1][:-1].split(',')
	rule = ('a', '>', 12345, 'A')
	rules = []
	for rr in raw_rules:
		if ':' not in rr:
			rules.append(('flow', rr))
			continue

		func = rr.split(':')
		then = func[1]

		operation = '>' if '>' in func[0] else '<'
		operands = func[0].split(operation)
		val = int(operands[1])
		cat = operands[0]

		rules.append(('rule', (cat, operation, val, then)))
	workflows[name] = rules


"""
in -> s<1351:px[a<2006:qkq:[x<1416, crn[x>2662]]]
"""

acceptable_part_ranges = []
def traverse(workflow, in_part):
	part = in_part.copy()
	num_combinations = 0

	for rule in workflow:
		kind, operation = rule
		if kind == 'flow':
			if  operation == 'A':
				acceptable_part_ranges.append(part)
			elif operation != 'R':
				traverse(workflows[operation], part)
			continue
		cat, comp, val, then = operation
		accept_split = 0
		reject_split = 0
		if comp == '<':
			accept_split = range(1, val)
			reject_split = range(val, part[cat][-1] + 1)
		else:
			accept_split = range(val + 1, part[cat][-1] + 1)
			reject_split = range(1, val + 1)
		part[cat] = reject_split
		if len(accept_split) == 0:
			continue
		accepted_part = part.copy()
		accepted_part[cat] = accept_split

		if then == 'A':
			acceptable_part_ranges.append(accepted_part)
		elif then != 'R':
			traverse(workflows[then], accepted_part)

		if len(reject_split) == 0:
			break

	return num_combinations


start = {
	'x': range(1, 4001),
	'm': range(1, 4001),
	'a': range(1, 4001),
	's': range(1, 4001)
}


traverse(workflows['in'], start)

def overlap(a, b):
	return range(max(a[0], b[0]), min(a[-1], b[-1])+1)

print(acceptable_part_ranges)
seen_part_ranges = []
cool = {}
combos = 0
for a, part in enumerate(acceptable_part_ranges):
	possible_combos = 1
	for cat in part.values():
		possible_combos *= len(cat)

	taken_combos = 0
	for b, r in enumerate(acceptable_part_ranges):
		n = min(a, b)
		m = max(a, b)
		if b == a:
			continue
		if (n, m) in cool:
			continue
		cool[(n, m)] = True
		print(n, m)

		nice = 1
		for cat in part.keys():
			ol = overlap(r[cat], part[cat])
			nice *= len(ol)
		taken_combos += nice
	combos += (possible_combos - taken_combos)
	seen_part_ranges.append(part)

print(combos)

167409079868000
109600266391206