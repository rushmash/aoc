#!/usr/bin/env python3

from itertools import product
import re

def drag_vx(v):
    return v-1 if v > 0 else v+1 if v < 0 else 0

def drag_vy(v):
    return v-1

input = open('in17.txt').read().strip()
target_square = list(map(int, re.findall('-?\d+', input)))
x1, x2, y1, y2 = target_square
r = max(map(abs, target_square))

velocities = 0
total_max_y = 0

for vx, vy in product([x for x in range(-r, r)], repeat=2):
    x, y = 0, 0
    max_y = 0
    velocities += 1

    while True:
        x += vx
        y += vy

        vx = drag_vx(vx)
        vy = drag_vy(vy)

        max_y = max(max_y, y)

        if x1 <= x <= x2 and y1 <= y <= y2:
            total_max_y = max(total_max_y, max_y)
            break
        elif x > x2 or y < y1:
            velocities -= 1
            break

print(total_max_y)
print(velocities)
