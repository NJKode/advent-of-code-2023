text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()
start_y = 0
start_x = 0

for l in range(len(lines)):
	line = lines[l]
	if 'S' in line:
		start_y = l
		start_x = line.index('S')
		break

start = (start_x, start_y)
loop_size = 1
direction = 'down' # TODO calculate this
next_loc = start

while True:
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

	loop_size += 1
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

print(int(loop_size/ 2))
