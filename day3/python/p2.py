import re

text_file = open("input-p2.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()




# store all symbol positions (x, y)
# run through numbers
num_map = [[]] * len(lines)

# build up symbol num_map
for l in range(len(lines)):
	num_map[l] = []
	line = lines[l]
	symbols = re.finditer('\d+', line)
	for match in symbols:
		start, end = match.span()
		for ind in range(start, end):
			num_map[l].append(ind)

def walk_l(y_loc, end_w):
	nums = num_map[y_loc]
	start_w = end_w
	x_loc = nums[start_w]
	while start_w > 0 and nums[start_w-1] == x_loc - 1:
		x_loc -= 1
		start_w -= 1
	return x_loc

def walk_r(y_loc, start_w):
	nums = num_map[y_loc]
	end_w = start_w
	x_loc = nums[start_w]
	while end_w < len(nums) - 1 and nums[end_w+1] == x_loc + 1:
		x_loc += 1
		end_w += 1
	x_loc += 1
	return x_loc

total = 0
for l in range(len(lines)):
	line = lines[l]
	max_width = len(line) - 1
	max_height = len(lines) - 1
	gears = re.finditer('\*', line)
	for match in gears:
		start, end = match.span()

		found_count = 0
		found_l = False
		found_r = False
		found_a = False
		found_b = False
		found_l_a = False
		found_l_b = False
		found_r_a = False
		found_r_b = False

		# look above
		if l > 0:
			if start in num_map[l - 1]:
				found_a = True
				found_count += 1

		# look below
		if l < max_height:
			if start in num_map[l + 1]:
				found_b = True
				found_count += 1

		# look left and right
		if start > 0:
			if (start - 1) in num_map[l]:
				found_count += 1
				found_l = True
			if found_a == False and l > 0 and (start - 1) in num_map[l - 1]:
				found_l_a = True
				found_count += 1
			if found_b == False and l < max_height and (start - 1) in num_map[l + 1]:
				found_l_b = True
				found_count += 1

		if start < max_width:
			if end in num_map[l]:
				found_r = True
				found_count += 1
			if found_a == False and l > 0 and end in num_map[l-1]:
				found_r_a = True
				found_count += 1
			if found_b == False and l < max_height and end in num_map[l + 1]:
				found_count += 1
				found_r_b = True

		if found_count == 2:
			start_s = 0
			end_s = 0
			num_s = ''
			nums_s = []
			if found_l == True:
				end_s = num_map[l].index(start-1)
				start_s = walk_l(l, end_s)
				nums_s.append(lines[l][start_s:start])
			if found_r == True:
				start_s = num_map[l].index(start + 1)
				end_s = walk_r(l, start_s)
				nums_s.append(lines[l][start+1:end_s])
			if found_a == True:
				known = num_map[l-1].index(start)
				start_s = walk_l(l-1, known)
				end_s = walk_r(l-1, known)
				nums_s.append(lines[l-1][start_s:end_s])
			if found_b == True:
				known = num_map[l+1].index(start)
				start_s = walk_l(l+1, known)
				end_s = walk_r(l+1, known)
				nums_s.append(lines[l+1][start_s:end_s])
			if found_l_a == True:
				end_s = num_map[l-1].index(start-1)
				start_s = walk_l(l-1, end_s)
				nums_s.append(lines[l-1][start_s:start])
			if found_r_a == True:
				start_s = num_map[l-1].index(start + 1)
				end_s = walk_r(l-1, start_s)
				nums_s.append(lines[l-1][start+1:end_s])
			if found_l_b == True:
				end_s = num_map[l+1].index(start-1)
				start_s = walk_l(l+1, end_s)
				nums_s.append(lines[l+1][start_s:start])
			if found_r_b == True:
				start_s = num_map[l+1].index(start + 1)
				end_s = walk_r(l+1, start_s)
				nums_s.append(lines[l+1][start+1:end_s])

			prod = int(nums_s[0]) * int(nums_s[1])
			total += prod




print(total)