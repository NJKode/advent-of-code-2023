text_file = open("input-p1-test.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()
patterns = []
new_pattern = []

# from here: https://stackoverflow.com/questions/2460177/edit-distance-in-python
def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

for line in lines:
	if len(line) == 0:
		patterns.append(new_pattern)
		new_pattern = []
	else:
		new_pattern.append(line)

patterns.append(new_pattern)

total_score = 0
for pattern in patterns:
	score = 0
	for y in range(1, len(pattern)):
		top_half = pattern[:y]
		bottom_half = pattern[y::]

		top_half.reverse()

		max_length = min(len(top_half), len(bottom_half))
		valid_reflection = True
		smudge_found = False
		for m in range(max_length):
			edit_distance = levenshteinDistance(top_half[m], bottom_half[m])
			if edit_distance == 1 and smudge_found == False:
				smudge_found = True
			elif edit_distance > 1 or (edit_distance == 1 and smudge_found == True):
				valid_reflection = False
				break

		if valid_reflection == True and smudge_found == True:
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
		smudge_found = False
		for m in range(max_length):
			edit_distance = levenshteinDistance(top_half[m], bottom_half[m])
			if edit_distance == 1 and smudge_found == False:
				smudge_found = True
			elif edit_distance > 1 or (edit_distance == 1 and smudge_found == True):
				valid_reflection = False
				break

		if valid_reflection == True and smudge_found == True:
			score = y
			break
	total_score += score


print(total_score)