import re

text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

expansion_factor = 2

lines = input.splitlines()

empty_y = []
empty_x_map = {}
empty_x = []
star_coords = []
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
			star_coords.append((s.start(), l))
			empty_x_map[s.start()] = False

for key, value in empty_x_map.items():
	if value == True:
		empty_x.append(key)

start_ind = 0
distances = []
while start_ind < len(star_coords) - 1:
	from_star = star_coords[start_ind]
	for s in range(start_ind + 1, len(star_coords)):
		to_star = star_coords[s]
		x_dist = abs(from_star[0] - to_star[0])
		y_dist = abs(from_star[1] - to_star[1])
		x_p = sorted([from_star[0], to_star[0]])
		y_p = sorted([from_star[1], to_star[1]])
		for x in empty_x:
			if x > x_p[0] and x < x_p[1]:
				x_dist += expansion_factor - 1
		for y in empty_y:
			if y > y_p[0] and y < y_p[1]:
				y_dist += expansion_factor - 1


		distance = x_dist + y_dist
		distances.append(distance)
	start_ind += 1


print(sum(distances))


