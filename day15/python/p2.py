import re
text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

matcher = re.finditer(r'[^,]+', input)
def getIndexOfLens(box, label):
	for i,lens in enumerate(box):
		if lens[0] == label:
			return i
	return -1

boxes = [[] for _ in range(256)]
for step_match in matcher:
	current_value = 0
	step = step_match.group(0)

	label_search = re.search('[a-zA-Z]+', step)
	label = label_search.group(0)
	instruction = step[label_search.end()]
	fs = step[label_search.end()+1::]
	focal_length = int(fs) if fs else -1

	for char in label:
		code = ord(char)
		current_value += code
		current_value *= 17
		current_value %= 256
	box_number = current_value

	lens_index = getIndexOfLens(boxes[box_number], label)
	if instruction == '=':
		if lens_index < 0:
			boxes[box_number].append((label, focal_length))
		else:
			boxes[box_number][lens_index] = (label, focal_length)
	elif lens_index >= 0:
		boxes[box_number] = boxes[box_number][:lens_index] + boxes[box_number][(lens_index + 1)::]

total_power = 0
for b in range(len(boxes)):
	box = boxes[b]
	for s in range(len(box)):
		lens = box[s]
		power = (1+b) * (1+s) * lens[1]
		total_power += power

print(total_power)