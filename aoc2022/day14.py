#!/usr/bin/env python3

from itertools import pairwise

traces = [[[int(z) for z in y.split(',')] \
                        for y in x.split(' -> ')] \
                            for x in open('in14.txt', 'r').read().splitlines()]

resting = set()
rocks = set()

max_rock_y = 0
source = (500, 0)

for path_trace in traces:
    for (_, y) in path_trace:
        max_rock_y = max(max_rock_y, y)

    for (x1, y1), (x2, y2) in pairwise(path_trace):
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        min_x = min(x1, x2)
        max_x = max(x1, x2)

        if x1 == x2:
            for y in range(min_y, max_y+1):
                rocks.add((x1, y))

        if y1 == y2:
            for x in range(min_x, max_x+1):
                rocks.add((x, y1))

def blocked(p):
    if p in resting or p in rocks or p[1] == max_rock_y + 2:
        return True
    
    return False

def try_move(p): 
    x, y = p
    for np in [(x, y+1), (x-1, y+1), (x+1, y+1)]:
        if not blocked(np):
            return np

    return p

p = source

part1_result = 0

while True:
    if not part1_result and p[1] == max_rock_y:
        part1_result = len(resting)

    np = try_move(p)
    if np != p:
        p = np
        continue

    if np == source:
        resting.add(np)
        break 

    resting.add(p)
    p = source

print(part1_result)
print(len(resting))