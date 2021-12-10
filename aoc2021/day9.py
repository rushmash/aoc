#!/usr/bin/env python3
from itertools import *
import math

lines = [[int(x) for x in l.strip()] for l in open('in9.txt', 'r')]
M = len(lines)
N = len(lines[0])

def get_lowest_indexes(height_map):
	lowest_i = []
	for line in height_map:
		prev = 9
		indexes = []
		for curr, next in pairwise(zip(chain(line, [9]), count(0))):
			if prev > curr[0] and curr[0] < next[0]:
				indexes.append(curr[1])
			prev = curr[0]
		lowest_i.append(indexes)
	return lowest_i

def part1():
	lowest_ir = get_lowest_indexes(lines)
	lowest_ic = get_lowest_indexes(zip(*lines))

	found = []
	for r, ri in zip(lowest_ir, count(0)):
		for c, ci in zip(lowest_ic, count(0)):
			if ci in r and ri in c:
				found.append(lines[ri][ci])

	return len(found) + sum(found)

def fill_basin(x, y, height_map) -> int:
	basin_area = 0
	if x >= N or y >= M or x < 0 or y < 0 or height_map[y][x] == 9:
		return 0
	else:
		basin_area +=1
		height_map[y][x] = 9

		basin_area += fill_basin(x+1, y, height_map)
		basin_area += fill_basin(x-1, y, height_map)
		basin_area += fill_basin(x, y+1, height_map)
		basin_area += fill_basin(x, y-1, height_map)
	return basin_area

def part2():
	basins = [fill_basin(y, x, lines) for y in range(M) for x in range(N)]
	return math.prod(sorted(basins)[-3:])

print(part1())
print(part2())
