#!/usr/bin/env python3

from collections import deque

points = set([tuple(int(y) for y in x.split(',')) for x in open('in18.txt', 'r').read().splitlines()])
moves = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]

exposed_part1 = len(points)*6
min_value = 1e2

for x, y, z in points:
    min_value = min(min_value, x, y, z)
    for dx, dy, dz in moves:
        if (x+dx, y+dy, z+dz) in points:
            exposed_part1 -= 1

outside_point = (min_value, min_value, min_value)
assert outside_point not in points

def find_enclosed(start, finish):
    Q = deque()
    Q.append(start)
    S = set()

    if start in points:
        return None

    while Q:
        x, y, z = Q.pop()
        if (x, y, z) == finish:
            return None
            
        if len(S) > len(points):
            return None

        if (x, y, z) in S:
            continue

        S.add((x, y, z))
        for dx, dy, dz in moves:
            p = (x+dx, y+dy, z+dz)
            if p not in points:
                Q.appendleft(p)
        
    return S

def enclosed_points():
    s = set()
    for x, y, z in points:
        for dx, dy, dz in moves:
            if e := find_enclosed((x+dx, y+dy, z+dz), outside_point):
                s = s.union(e)
    return s

enclosed = enclosed_points()
exposed_part2 = exposed_part1

for x, y, z in points:
    for dx, dy, dz in moves:
        if (x+dx, y+dy, z+dz) in enclosed:
            exposed_part2 -= 1

print(exposed_part1)
print(exposed_part2)