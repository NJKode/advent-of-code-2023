text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()
patterns = []
new_pattern = []

for line in lines:
	if len(line) == 0:
		patterns.append(new_pattern)
		new_pattern = []
	else:
		new_pattern.append(line)

patterns.append(new_pattern)

# find horizontal reflection
total_score = 0
for pattern in patterns:
	score = 0
	for y in range(1, len(pattern)):
		top_half = pattern[:y]
		bottom_half = pattern[y::]

		top_half.reverse()

		max_length = min(len(top_half), len(bottom_half))
		valid_reflection = True
		for m in range(max_length):
			if (top_half[m] != bottom_half[m]):
				valid_reflection = False
				break

		if valid_reflection == True:
			score = y * 100
			break

	total_score += score
	if score != 0:
		continue

	lenth = len(pattern)
	pattern_t = []
	for c in range(len(pattern[0])):
		line = ''
		for y in range(len(pattern)):
			line = pattern[y][c] + line
		pattern_t.append(line)

	for y in range(1, len(pattern_t)):
		top_half = pattern_t[:y]
		bottom_half = pattern_t[y::]

		top_half.reverse()

		max_length = min(len(top_half), len(bottom_half))
		valid_reflection = True
		for m in range(max_length):
			if (top_half[m] != bottom_half[m]):
				valid_reflection = False
				break

		if valid_reflection == True:
			score = y
			break
	total_score += score


print(total_score)