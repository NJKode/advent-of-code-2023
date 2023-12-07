text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

max_red = 12
max_green = 13
max_blue = 14

games = input.splitlines()

total = 0

for i in range(len(games)):
	game = games[i]
	game_id = i + 1
	unprocessed_sets = game.split(':')[1].strip()
	sets = unprocessed_sets.split(';')

	invalid_flag = False

	for set_cubes in sets:
		shown = {
			'blue': 0,
			'red': 0,
			'green': 0
		}
		cubes = set_cubes.strip().split(',')
		for cube in cubes:
			cube_info = cube.strip().split(' ')
			num_cubes_s = cube_info[0]
			colour = cube_info[1]
			num_cubes = int(num_cubes_s)

			shown[colour] = num_cubes

		if shown['red'] > max_red or shown['green'] > max_green or shown['blue'] > max_blue:
			invalid_flag = True

	if invalid_flag == False:
		total += game_id

print(total)


