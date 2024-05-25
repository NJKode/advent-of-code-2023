import re
text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()

start = (0, 0)
current_pos = start
c_x = []
c_y = []

minX = 0
minY = 0

dir_map = {
	'0': 'R',
	'1': 'D',
	'2': 'L',
	'3': 'U'
}

corners = []
total_length = 0
for line in lines:
	c_x.append(current_pos[0])
	c_y.append(current_pos[1])
	parts = line.split('#')
	hex_code = parts[1][:-2]
	dir_code = parts[1][-2]

	length = int(hex_code, 16)
	direction = dir_map[dir_code]

	x, y = current_pos
	if direction == 'U':
		current_pos = (x, y + length)
		total_length += length
	elif direction == 'D':
		current_pos = (x, y - length)
	elif direction == 'L':
		total_length += length
		current_pos = (x - length, y)
	elif direction == 'R':
		current_pos = (x + length, y)

	minX = min(minX, current_pos[0])
	minY = min(minY, current_pos[1])

area = 0

for i_x in range(len(c_x)):
	i_y = -1 if i_x + 1 == len(c_x) else i_x + 1
	area += (c_x[i_x] * c_y[i_y])

for i_y in range(len(c_y)):
	i_x = -1 if i_y + 1 == len(c_y) else i_y + 1
	area -= (c_x[i_x] * c_y[i_y])

area = int(abs(area) / 2)


answer = 952408144115
area = area + total_length + 1
print(area)