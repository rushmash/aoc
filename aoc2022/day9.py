#!/usr/bin/env python3

input = open('in9.txt', 'r').read().splitlines()

def touching(p1, p2):
    x1, y1, x2, y2 = (*p1, *p2)
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

def move(p, x, y):
    for _ in range(abs(x)):
        px, py = p
        p = px + x//abs(x), py
        yield p

    for _ in range(abs(y)):
        px, py = p
        p = px, py + y//abs(y)
        yield p

def follow(p1, p2):
    if not touching(p1, p2):
        x1, y1, x2, y2 = (*p1, *p2)
        dx = 1 if x1 > x2 else -1
        dy = 1 if y1 > y2 else -1

        if x1 == x2:
            *_, p = move(p2, 0, dy)
        elif y1 == y2:
            *_, p = move(p2, dx, 0)
        else:
            *_, p = move(p2, dx, dy)
        return p
    return p2
        
rope = [(0, 0) for _ in range(10)]
positions1 = set()
positions2 = set()

for motion in input:
    match motion.split():
        case 'R', step:
            dx, dy = int(step), 0
        case 'U', step:
            dx, dy = 0, -int(step)
        case 'L', step:
            dx, dy = -int(step), 0
        case 'D', step:
            dx, dy = 0, int(step)

    for head in move(rope[0], dx, dy):
        rope[0] = head
        for i in range(1, len(rope)):
            rope[i] = follow(rope[i-1], rope[i])

        positions1.add(rope[1])
        positions2.add(rope[-1])

print(len(positions1))
print(len(positions2))