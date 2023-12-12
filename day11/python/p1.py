import re

text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()

empty_y = []
empty_x_map = {}
empty_x = []
for s in range(len(lines[0])):
	empty_x_map[s] = True

for l in range(len(lines)):
	line = lines[l]
	star_search = re.finditer(r'#', line)
	nice = list(star_search)

	if len(nice) == 0:
		empty_y.append(l)
	else:
		for s in nice:
			empty_x_map[s.start()] = False

for key, value in empty_x_map.items():
	if value == True:
		empty_x.append(key)

# expand
empty_y.reverse()
empty_x.reverse()
universe = []
next_empty_y = empty_y.pop() if len(empty_y) > 0 else -1

for l in range(len(lines)):
	y_string = lines[l]
	for x in empty_x:
		y_string = y_string[:x] + '.' + y_string[x:]

	universe.append(y_string)
	if next_empty_y >= 0 and l == next_empty_y:
		universe.append(y_string)
		next_empty_y = empty_y.pop() if len(empty_y) >= 1 else -1

star_coords = []
for y in range(len(universe)):
	line = universe[y]
	star_search = re.finditer(r'#', line)
	nice = list(star_search)
	for s in nice:
		star_coords.append((s.start(), y))

start_ind = 0
distances = []
while start_ind < len(star_coords) - 1:
	from_star = star_coords[start_ind]
	for s in range(start_ind + 1, len(star_coords)):
		to_star = star_coords[s]
		distance = abs(from_star[0] - to_star[0]) + abs(from_star[1] - to_star[1])
		distances.append(distance)
	start_ind += 1

print(sum(distances))


