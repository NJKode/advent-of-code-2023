text_file = open("input-p1.txt", "r")
input = text_file.read()
text_file.close()

modules = {}
conjunction_map = {}

lines = input.splitlines()

for line in lines:
	parts = line.split(' -> ')
	module = parts[0]
	receivers = parts[1].split(', ')

	type = ''
	name = ''
	state = 0
	if module == 'broadcaster':
		type = 'broadcaster'
		name = type
	elif module[0] == '%':
		type = 'flip'
		name = module[1::]
	elif module[0] == '&':
		type = 'conj'
		name = module[1::]
		conjunction_map[name] = {}

	modules[name] = (type, state, receivers)

for name, (type, state, receivers) in modules.items():
	for r in receivers:
		if r in conjunction_map:
			conjunction_map[r][name] = 0
			break

end_mod = 'qq'

low_pulse_count = 0
high_pulse_count = 0
run_count = 0

while modules[end_mod][1] != 1:
	run_count += 1
	initial_pulse = ('button', 'broadcaster', 0)
	pulse_queue = [initial_pulse]
	while len(pulse_queue) > 0:
		sender, mod_name, pulse = pulse_queue[0]
		pulse_queue = pulse_queue[1::]

		if pulse == 1:
			high_pulse_count += 1
		else:
			low_pulse_count += 1

		if mod_name not in modules:
			continue
		module = modules[mod_name]
		type, state, receivers = module

		if type == 'broadcaster':
			for r in receivers:
				pulse_queue.append((mod_name, r, pulse))
		elif type == 'flip':
			if pulse == 0:
				new_pulse = 1 - state
				modules[mod_name] = (type, new_pulse, receivers)
				for r in receivers:
					pulse_queue.append((mod_name, r, new_pulse))
		elif type == 'conj':
			conjunction_map[mod_name][sender] = pulse
			inputs = conjunction_map[mod_name]
			new_pulse = 0
			for i_name, i_pulse in inputs.items():
				if i_pulse == 0:
					new_pulse = 1
					break
			for r in receivers:
					pulse_queue.append((mod_name, r, new_pulse))

print(run_count)