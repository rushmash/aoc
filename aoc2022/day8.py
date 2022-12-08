#!/usr/bin/env python3

from itertools import product
from functools import reduce

def view_distance(trees, height):
    distance = 0
    for tree_height in trees:
        distance += 1
        if height <= tree_height:
            break
    return distance

def transpose(M):
    return [[M[j][i] for j in range(len(M[0]))] for i in range(len(M))]

grid = [[int(c) for c in line] for line in open('in8.txt', 'r').read().splitlines()]
trans_grid = transpose(grid)

visible_trees = 0
max_scenic_score = 0

for p in product(range(len(grid)), repeat=2):
    if min(p) == 0 or max(p) == len(grid)-1:
        visible_trees += 1
        continue

    x, y = p
    height = grid[x][y]

    trees_left = grid[x][y+1:]
    trees_right = list(reversed(grid[x][:y]))
    trees_up = trans_grid[y][x+1:]
    trees_down = list(reversed(trans_grid[y][:x]))

    if max(trees_left)  < height or \
       max(trees_right) < height or \
       max(trees_up)    < height or \
       max(trees_down)  < height:
        visible_trees += 1

    max_scenic_score = max(max_scenic_score, reduce(lambda x,y: x*y, [
        view_distance(trees_left, height),
        view_distance(trees_right, height),
        view_distance(trees_up, height),
        view_distance(trees_down, height),
    ]))

print(visible_trees)
print(max_scenic_score)
