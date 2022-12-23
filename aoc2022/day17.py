#!/usr/bin/env python3

instructions = open('in17.txt', 'r').readline()
figures = [
	[[1,1,1,1]],
	[[0,1,0],[1,1,1],[0,1,0]],
	[[1,1,1],[0,0,1],[0,0,1]],
	[[1],[1],[1],[1]],
	[[1,1], [1,1]]
]

def get_shift(shape, shift, i):
	if instructions[i%len(instructions)] == '<':
		return max(0, shift-1)
	else:
		return min(7-len(shape[0]), shift+1)

def valid(shape, shift, field, depth):
	for f, s in zip(reversed(range(depth)), range(len(shape))):
		for k in range(len(shape[s])):
			if field[len(field)-1-f][shift + k] & shape[s][k]:
				return False
	return True

def place(shape, shift, field, depth):
	s = - 1
	for f, s in zip(reversed(range(depth)), range(len(shape))):
		for k in range(len(shape[s])):
			field[len(field)-1-f][shift + k] |= shape[s][k]

	for i in range(s+1, len(shape)):
		row = [0,0,0,0,0,0,0]
		for k in range(len(shape[i])):
			row[shift + k] |= shape[i][k]
		field.append(row)

def show(f):
	for line in reversed(f):
		for v in line:
			print('#' if v else ' ', end='')
		print()
	print()

def state(field):
	compare_size = 20
	flat = []
	[flat.extend(x) for x in field[-compare_size:]]
	return ''.join([str(x) for x in flat])

def tower_height(iterations):
	field = [[1,1,1,1,1,1,1], [1,1,1,1,1,1,1]]
	figure_it = 0
	instr_it = 0

	seen = {}
	skipped_height = 0
	padding = len(field)

	it = 0
	while it < iterations:
		# show(field)
		field_state = (instr_it%len(instructions), figure_it%len(figures), state(field))
		if not skipped_height and field_state in seen:
			prev_height, prev_it = seen[field_state]

			steps = it - prev_it
			skipped_height = (len(field) - prev_height) * ((iterations - it) // steps)
			iterations = it + (iterations - it) % steps 
		seen[field_state] = (len(field), it)

		shape = figures[figure_it%len(figures)]
		figure_it += 1

		shift = 2
		for _ in range(4):
			shift = get_shift(shape, shift, instr_it)
			instr_it += 1

		for depth in range(1, len(field)):
			if not valid(shape, shift, field, depth):
				place(shape, shift, field, depth-1)
				break

			prev_shift = shift
			shift = get_shift(shape, shift, instr_it)
			instr_it += 1

			if not valid(shape, shift, field, depth):
				shift = prev_shift
				
		it += 1

	return len(field[padding:]) + skipped_height

print(tower_height(2022))
print(tower_height(1000000000000))
