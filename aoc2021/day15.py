#!/usr/bin/env python3
from heapq import *

input = [[int(y) for y in x] for x in open('in15.txt', 'r').read().splitlines()]

def shortest_path_length(M):
	# Dijkstra

	dx = (-1,0,1,0)
	dy = (0,1,0,-1)

	M_SIZE = len(M) - 1

	D = [[1e50 for _ in M] for _ in M]
	P = {}

	Q = []
	heapify(Q)
	D[0][0] = 0

	for xi, x in enumerate(D):
		for yi, y in enumerate(x):
			heappush(Q, (y, xi, yi))

	while Q:
		v, vx, vy = heappop(Q)
		if (vx, vy) == (M_SIZE, M_SIZE):
			break

		for x, y in zip(dx, dy):
			if 0 <= vx + x <= M_SIZE and 0 <= vy + y <= M_SIZE:
				alt = D[vx][vy] + M[vx + x][vy + y]

				if alt < D[vx + x][vy + y]:
					D[vx + x][vy + y] = alt
					P[(vx + x, vy + y)] = (vx, vy)
					heappush(Q, (alt, vx + x, vy + y))

	r = 0
	x, y = M_SIZE, M_SIZE
	while (x, y) != (0, 0):
		r += M[x][y]
		x, y = P[(x, y)]

	return r

def expand(grid):
	inc = lambda n, x: (x + n) % 9 if x + n >= 10 else x + n
	enl = [[inc(i, x) for x in line] for i in range(0, 5) for line in grid]

	for line in enl:
		line.extend([inc(k, y) for k in range(1, 5) for y in line])

	return enl

print(shortest_path_length(input))
print(shortest_path_length(expand(input)))