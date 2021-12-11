#!/usr/bin/env python3
from itertools import *

def model(oct_grid, max_iterations, find_sync=False) -> int:
    M = len(oct_grid)
    N = len(oct_grid[0])

    MM = [-1, 0, 1, 0, 1, 1, -1, -1]
    NN = [0, -1, 0, 1, 1, -1, -1, 1]
    count = 0

    for it in range(1, max_iterations+1):
        to_flash = set()
        flashed = set()
        for m in range(M):
            for n in range(N):
                if (m, n) in flashed:
                    continue

                oct_grid[m][n] += 1
                if oct_grid[m][n] > 9:
                    to_flash.add((m,n))

        while to_flash:
            m, n = to_flash.pop()
            flashed.add((m,n))
            oct_grid[m][n] = 0
            for i in range(len(MM)):
                mm = m + MM[i]
                nn = n + NN[i]
                if 0 <= mm < M and 0 <= nn < N and not (mm, nn) in flashed:
                    oct_grid[mm][nn] += 1
                    if oct_grid[mm][nn] > 9:
                        to_flash.add((mm,nn))

        count += len(flashed)
        if find_sync and all(x == 0 for x in chain(*oct_grid)):
            break
    return it if find_sync else count

def part1():
    grid = [[int(n) for n in l.strip()] for l in open('in11.txt', 'r')]
    return model(grid, 100)

def part2():
    grid = [[int(n) for n in l.strip()] for l in open('in11.txt', 'r')]
    return model(grid, 100000, find_sync=True)

print(part1())
print(part2())
