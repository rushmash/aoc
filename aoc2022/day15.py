#!/usr/bin/env python3

import re

input = [[*map(int, re.findall('-?\d+', x))] for x in open('in15.txt', 'r').read().splitlines()]

manhattan_distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

sensors = []
beacons = set()
for xs, ys, xb, yb in input:
    sensors.append(((xs, ys, xb, yb), manhattan_distance((xs, ys), (xb, yb))))
    beacons.add((xb, yb))

def normalize(segments):
    ss = []
    prev = None
    for (x3, x4) in sorted(segments):
        if not prev:
            prev = (x3, x4)
            continue

        (x1, x2) = prev
        if x1 == x3:
            prev = (x3, x4)
        elif x2 >= x4:
            prev = (x1, x2)
        elif x2 >= x3:
            prev = (x1, x4)
        else:
            ss.append(prev)
            prev = (x3, x4)

    ss.append(prev)
    return ss

def xscan_range(y):
    segments = []
    for (xs, ys, _, _), md in sensors:
        if not ys-md <= y <= ys+md:
            continue

        if ys+md == y or ys-md == y:
            segments.append((y, y))
            continue

        if y < ys:
            s = md-ys+y
        elif y > ys:
            s = md+ys-y
        else:
            s = md

        segments.append((xs-s, xs+s))

    return normalize(segments)

def segments_length(r):
    cnt = 0
    for x1, x2 in r:
        cnt += x2+1-x1
    return cnt

def part1():
    scan_y = 2000000
    scanned_segments = xscan_range(scan_y)
    positions = segments_length(scanned_segments)
    for xb, yb in beacons:
        for x1, x2 in scanned_segments:
            if yb == scan_y and x1 <= xb <= x2:
                positions -= 1
    return positions

def part2():
    n = 4000000
    for y in range(n):
        scanned_segments = xscan_range(y)
        if len(scanned_segments) >= 2:
            x2_prev = None
            for x1, x2 in scanned_segments:
                if not x2_prev:
                    x2_prev = x2
                elif x1 - x2_prev == 2:
                    return (x2_prev + 1) * n + y

print(part1())
print(part2())