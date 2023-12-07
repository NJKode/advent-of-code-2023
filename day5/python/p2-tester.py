import re

text_file = open("input-p1-test.txt", "r")
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

possible_location = 59
from_source = possible_location
print('trialing location:', possible_location)
viable_seed = False

for p in range(len(parts)):
	p_index = len(parts) - 1 - p
	maps = parts[p_index]
	prev = from_source

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
		print('Caught from', destination_start, ', range:', map_range)
		from_source += map_diff
		print('New value:', from_source)
		break

	if prev == from_source:
			print('No mapping. Remains:', from_source)


seed_num = from_source

s = 0
while s < len(seeds):
	seed_start = seeds[s]
	seed_end = seeds[s + 1] + seed_start

	if seed_num >= seed_start and seed_num < seed_end:
		print('Within seed range', seed_start, '-', seeds[s + 1])
		viable_seed = True
		s = len(seeds_s) + 1
		print(possible_location, ' was a viable location')


	s += 2

if viable_seed == False:
	print(possible_location, ' was NOT a viable location')


# take any boundary
# look up to see if it's a valid seed
# if it is, look down and track its location
# repeat with all boundaries at all depths. Keep smallest location
# remain with