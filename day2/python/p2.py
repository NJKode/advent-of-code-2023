text_file = open("input-p2.txt", "r")
input = text_file.read()
text_file.close()

games = input.splitlines()
total = 0

for i in range(len(games)):
	game = games[i]
	game_id = i + 1
	unprocessed_sets = game.split(':')[1].strip()
	sets = unprocessed_sets.split(';')

	max_shown = {
		'blue': 0,
		'red': 0,
		'green': 0
	}
	for set_cubes in sets:
		cubes = set_cubes.strip().split(',')
		for cube in cubes:
			cube_info = cube.strip().split(' ')
			num_cubes_s = cube_info[0]
			colour = cube_info[1]
			num_cubes = int(num_cubes_s)

			if num_cubes > max_shown[colour]:
				max_shown[colour] = num_cubes

	power = max_shown['red'] * max_shown['blue'] * max_shown['green']
	total += power

print()

print(total)


