#!/usr/bin/env python3
from collections import defaultdict
from collections import Counter
from itertools import *

m = defaultdict(list)
for line in open('in12.txt', 'r'):
	p1, p2 = line.strip().split('-')
	m[p1].append(p2)
	m[p2].append(p1)

def find_paths(twice=False):
	paths = [['start']]
	found = []

	while paths:
		path = paths.pop()
		if path[-1] == 'end':
			found.append(path)
			continue

		for p in m[path[-1]]:
			if p == 'start':
				continue

			if p.islower():
				if twice:
					p_count = Counter(filter(str.islower, path))
					if p_count[p] >= 1 and any(x > 1 for x in p_count.values()):
						continue

				elif p in path:
					continue

			paths.append(path + [p])
	return found

def part1():
	return len(find_paths())

def part2():
	return len(find_paths(True))

print(part1())
print(part2())
