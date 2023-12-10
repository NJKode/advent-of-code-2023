import re

text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()
total = 0

start_y = 0
start_x = 0
loop = []

for l in range(len(lines)):
	line = lines[l]
	search = re.search('S', line)
	if search != None:
		start_y = l
		start_x = search.start()
		break

start = (start_x, start_y)
loop.append(start)

direction = 'down' # TODO calculate this
next_loc = start

steps = 0
while True:
	print(next_loc)
	steps += 1
	if direction == 'up':
		next_loc = (next_loc[0], next_loc[1] - 1)
	elif direction == 'down':
		next_loc = (next_loc[0], next_loc[1] + 1)
	elif direction == 'left':
		next_loc = (next_loc[0] - 1, next_loc[1])
	elif direction == 'right':
		next_loc = (next_loc[0] + 1, next_loc[1])

	if next_loc == start:
		break

	loop.append(next_loc)

	next_pipe = lines[next_loc[1]][next_loc[0]]

	if next_pipe == '-' or next_pipe == '|':
		direction = direction
	elif direction == 'right':
		direction = 'down' if next_pipe == '7' else 'up'
	elif direction == 'left':
		direction = 'down' if next_pipe == 'F' else 'up'
	elif direction == 'up':
		direction = 'right' if next_pipe == 'F' else 'left'
	elif direction == 'down':
		direction = 'right' if next_pipe == 'L' else 'left'


loop_size = len(loop)
print(loop_size / 2)