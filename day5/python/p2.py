import re

text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.split('\n')

seed_string = lines[0]

index = 0
parts = [[] for _ in range(7)]
for line in lines[3:999]:
	if line == '':
		continue
	elif re.match('^\d', line):
		parts[index].append(line)
	else:
		index += 1

#seed_to_soil
seeds = []
seeds_s = seed_string.split(':')[1].split()
for seed_s in seeds_s:
	seeds.append(int(seed_s))

viable_seed = False
possible_location = 0
while not viable_seed:
	if possible_location % 1000000 == 0:
		print(possible_location)
	from_source = possible_location
	for p in range(len(parts)):
		p_index = len(parts) - 1 - p
		maps = parts[p_index]

		for locs in maps:
			map_parts = locs.split()
			destination_start = int(map_parts[0])

			if from_source < destination_start:
				continue
			map_range = int(map_parts[2])

			if from_source > destination_start + map_range - 1:
				continue

			source_start = int(map_parts[1])
			map_diff = source_start - destination_start
			from_source += map_diff
			break

	seed_num = from_source

	s = 0
	while s < len(seeds):
		seed_start = seeds[s]
		seed_end = seeds[s + 1] + seed_start

		if seed_num >= seed_start and seed_num < seed_end:
			viable_seed = True
			s = len(seeds_s) + 1
			print(possible_location)

		s += 2

	possible_location += 1


