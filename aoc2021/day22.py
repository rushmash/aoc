#!/usr/bin/env python3
import re
from itertools import product
from dataclasses import dataclass

@dataclass(frozen=True)
class Cuboid:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

    def volume(self):
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1)

    def intersect(self, cub):
        x1 = max(self.x1, cub.x1)
        x2 = min(self.x2, cub.x2)
        y1 = max(self.y1, cub.y1)
        y2 = min(self.y2, cub.y2)
        z1 = max(self.z1, cub.z1)
        z2 = min(self.z2, cub.z2)

        if x1 > x2 or y1 > y2 or z1 > z2:
            return None

        return Cuboid(x1, x2, y1, y2, z1, z2)

    def substract(self, cub):
        intersection = self.intersect(cub)
        if intersection is None:
            return [self]

        x_regions = [(self.x1, intersection.x1 - 1), (intersection.x1, intersection.x2), (intersection.x2 + 1, self.x2)]
        y_regions = [(self.y1, intersection.y1 - 1), (intersection.y1, intersection.y2), (intersection.y2 + 1, self.y2)]
        z_regions = [(self.z1, intersection.z1 - 1), (intersection.z1, intersection.z2), (intersection.z2 + 1, self.z2)]

        surrounding_cuboids = []
        for xi, yi, zi in product([0, 1, 2], repeat=3):
            if xi == 1 and yi == 1 and zi == 1:
                continue

            x_range, y_range, z_range = x_regions[xi], y_regions[yi], z_regions[zi]
            surrounding_cuboids.append(Cuboid(*x_range, *y_range, *z_range))

        return list(filter(lambda c:
                            self.x1 <= c.x1 and c.x2 <= self.x2 and
                            self.y1 <= c.y1 and c.y2 <= self.y2 and
                            self.z1 <= c.z1 and c.z2 <= self.z2, surrounding_cuboids))

def parse_input():
    for line in open('aoc2021/in22.txt').read().splitlines():
        cuboid = Cuboid(*list(map(int, re.findall("-?\\d+", line))))
        yield ('on' if line.startswith('on') else 'off', cuboid)

on_cuboids = set()

for cmd, new_cuboid in parse_input():
    match cmd:
        case 'on':
            new_cuboids = [new_cuboid]
            for existing_cub in on_cuboids:
                new_pieces = []
                for piece in new_cuboids:
                    new_pieces.extend(piece.substract(existing_cub))
                new_cuboids = new_pieces
            on_cuboids.update(new_cuboids)

        case 'off':
            new_pieces = set()
            for existing_cub in on_cuboids:
                new_pieces.update(existing_cub.substract(new_cuboid))
            on_cuboids = new_pieces

volume_under50 = 0
volume = 0
for c in on_cuboids:
    vol = c.volume()
    if not any(map(lambda x: abs(x) > 50, [c.x1, c.x2, c.y1, c.y2, c.z1, c.z2])):
        volume_under50 += vol
    volume += vol

# pypy3 ~ 4min
print(volume_under50)
print(volume)
