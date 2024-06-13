text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

lines = input.splitlines()
map = [[[]]]

for b, line in enumerate(lines):
	parts = line.split('~')
	start = parts[0]
	end = parts[0]

	start = parts[0].split(',')
	end = parts[1].split(',')

	s_x = int(start[0])
	s_y = int(start[1])
	s_z = int(start[2])

	e_x = int(end[0])
	e_y = int(end[1])
	e_z = int(end[2])

	if s_x != e_x:
