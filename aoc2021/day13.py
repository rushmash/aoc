#!/usr/bin/env python3
from itertools import *

folds = []
dots = []
with open('in13.txt', 'r') as f:
	for line in f:
		l = line.strip()
		if ',' in l:
			a, b = l.split(',')
			dots.append((int(a), int(b)))
		elif 'fold along x' in l:
			pos = int(l.split('=')[-1])
			folds.append(lambda x, y, pos=pos: (pos*2 - x if x > pos else x, y))
		elif 'fold along y' in l:
			pos = int(l.split('=')[-1])
			folds.append(lambda x, y, pos=pos: (x, pos*2 - y if y > pos else y))

def part1():
	print(len({folds[0](*dot) for dot in dots}))

def part2():
	new = set(dots)
	for f in folds:
		new = {f(*dot) for dot in new}

	X = max([x for x, y in new])
	Y = max([y for x, y in new])

	for y in range(Y+1):
		line = ''
		for x in range(X+1):	
			if (x, y) in new:
				line += '#'
			else:
				line += ' '
		print(line)

part1()
part2()
