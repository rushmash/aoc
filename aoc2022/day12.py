#!/usr/bin/env python3

from collections import deque
from itertools import product

input = open('in12.txt', 'r').read().splitlines()

def value(c):
	match c:
		case 'S':
			return ord('a') - ord('a')
		case 'E':
			return ord('z') - ord('a')

	return ord(c) - ord('a')

def distance(a, b):
	return value(b) - value(a)

def shortest_path(M, start_points, end):
	# bfs

	MX = len(M) - 1
	MY = len(M[0]) - 1

	Q = deque()
	S = set()
	for p in start_points:
		Q.append((0, p))
		S.add(p)

	while Q:
		e, (x, y) = Q.popleft()
		for xx, yy in [(x-1,y), (x,y+1), (x+1,y), (x,y-1)]:
			if 0 <= xx <= MX and 0 <= yy <= MY and not (xx,yy) in S and distance(M[x][y], M[xx][yy]) <= 1:
				if (xx, yy) == end:
					return e+1

				Q.append((e+1, (xx, yy)))
				S.add((xx,yy))

points = []
for x, y in product(range(len(input)), range(len(input[0]))):
	match input[x][y]:
		case 'S':
			start = (x, y)
		case 'E':
			end = (x, y)
		case 'a':
			points.append((x, y))

print(shortest_path(input, [start], end))
print(shortest_path(input, points, end))