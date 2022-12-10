#!/usr/bin/env python3

input = open('in10.txt', 'r').read().splitlines()

X = 1
cycles = [0]

for instr in input:
    match instr.split():
        case ['noop']:
            cycles.append(X)
        case ['addx', v]:
            cycles.append(X)
            cycles.append(X)
            X += int(v)

s = 0
for i in range(20, 221, 40):
    s += cycles[i] * i
print(s)

for cycle, x in enumerate(cycles[1:], 1):
    row_pos = cycle % 40
    pixel = '#' if row_pos in map(lambda a: a+x, [0, 1, 2]) and row_pos != 0 else ' '
    print(pixel, end='' if cycle % 40 != 0 else '\n')
