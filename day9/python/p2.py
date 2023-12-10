text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()
total = 0

for line in lines:
	numbers_s = line.split()
	initial_numbers = []
	for number_s in numbers_s:
		initial_numbers.append(int(number_s))

	found = False
	edge_diffs = []

	line_nums = initial_numbers.copy()
	while not found:
		diffs = []
		all_zeroes = True
		for l in range(len(line_nums) - 1):
			diff = line_nums[l + 1] - line_nums[l]
			diffs.append(diff)

			if diff != 0:
				all_zeroes = False
		edge_diffs.append(diffs[0])

		if all_zeroes == True:
			found = True
		else:
			line_nums = diffs.copy()

	edge_diffs.reverse()

	new_diff = 0
	for d in edge_diffs:
		new_diff = d - new_diff

	extrapolated = initial_numbers[0] - new_diff
	total += extrapolated

print(total)
