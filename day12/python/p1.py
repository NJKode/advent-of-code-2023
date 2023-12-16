import re
from itertools import combinations
text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

def validate_string(test_string, case_string):
	if len(test_string) != len(case_string):
		return False

	real_chars = re.finditer(r'\.|#')
	for char in real_chars:
		ind = char.start()
		if test_string[ind] != real_chars[ind]:
			return False
	return True

lines = input.splitlines()
total_combinations = 0

for line in lines:
	parts = line.split()
	case_string = parts[0]
	case_length = len(case_string)

	nums_s = re.findall(r'\d+', parts[1])
	springs = []
	for num_s in nums_s:
		springs.append(int(num_s))

	gaps = [1] * (len(springs) - 1)
	spaces_required = sum(springs) + len(springs) - 1
	empty_spaces = case_length - spaces_required

	opts = combinations(range(len(springs)+empty_spaces), len(springs))

	required_indeces = []
	matches = re.finditer(r'#|\.', line)
	for match in matches:
		sp = False if match.group(0) == '.' else True
		required_indeces.append((match.start(), sp))

	num_combinations = 0
	for opt in list(opts):
		row = []
		gaps = [0] + list(opt)
		for s in range(len(springs)):
			gap = gaps[s + 1] - gaps[s]
			row += ([False] * gap)
			row += [True] * springs[s]

		space_remaining = case_length - len(row)
		row += [False] * space_remaining

		valid = True
		for rq in required_indeces:
			if row[rq[0]] != rq[1]:
				valid = False
				break

		if valid == True:
			num_combinations += 1

	print(f'{line} | {num_combinations}')
	total_combinations += num_combinations

print(total_combinations)