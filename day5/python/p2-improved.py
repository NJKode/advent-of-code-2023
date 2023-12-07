import time
import re
start_time = time.perf_counter_ns()
print('Timer started')

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


# loop from bottom to top [p_level]
# 	find all lower bounds
#	for each lower bound
#		loop up to see if valid seed (from p_level)
#		if valid, loop down (from p_level) and record location
# 	move p_level up

lowest_location = -1

for p in range(len(parts)):
# if True:
	p_index = len(parts) - 1 - p
	map_lines = parts[p_index]

	lower_boundaries = []
	lower_boundaries.append(0)
	for locs in map_lines:
		map_parts = locs.split()
		destination_start = int(map_parts[0])
		lower_boundaries.append(destination_start)

		map_range = int(map_parts[2])
		next_start = destination_start + map_range
		lower_boundaries.append(next_start)

		#remove dupes
		lower_boundaries = list(set(lower_boundaries))

	# loop up to find viable seed
	for b in lower_boundaries:
		level = p_index
		from_source = b
		viable_seed = False
		while level >= 0:
			maps = parts[level]

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

			level -= 1

		seed_num = from_source

		# check viable seed
		s = 0
		while s < len(seeds):
			seed_start = seeds[s]
			seed_end = seeds[s + 1] + seed_start

			if seed_num >= seed_start and seed_num < seed_end:
				viable_seed = True
				s = len(seeds_s) + 1 # breaks loop
			s += 2


		next_marker = b
		if viable_seed == True:

			for level in range(p_index + 1, len(parts)):
				maps = parts[level]

				for locs in maps:
					map_parts = locs.split()
					source_start = int(map_parts[1])

					if source_start > next_marker:
						continue

					map_range = int(map_parts[2])
					if next_marker > source_start + map_range:
						continue

					# within range
					destination_start = int(map_parts[0])
					map_diff = destination_start - source_start
					next_marker += map_diff
					break

			final_location = next_marker
			if lowest_location < 0 or final_location < lowest_location:
				lowest_location = final_location

print('---------------')
print(lowest_location)
print('---------------')


end_time = time.perf_counter_ns()

ns_time = end_time - start_time

elapsed_time = ns_time / 1000000
print('Time elapsed:', elapsed_time, 'ms')

# take any boundary
# look up to see if it's a valid seed
# if it is, look down and track its location
# repeat with all boundaries at all depths. Keep smallest location
# remain with