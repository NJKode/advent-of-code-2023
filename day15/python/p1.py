import re
text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

matcher = re.finditer(r'[^,]+', input)

code_sum = 0
for step_match in matcher:
	current_value = 0
	step = step_match.group(0)
	for char in step:
		code = ord(char)
		current_value += code
		current_value *= 17
		current_value %= 256
	step_hash = current_value
	# print(step, step_hash)
	code_sum += step_hash

print(code_sum)