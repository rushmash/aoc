#!/usr/bin/env python3

data = open('in20.txt').read().split('\n\n')
algorithm_data = data[0]
image_data = [list(x) for x in data[1].splitlines()]

MAX_ENHANCEMENT = 50

def count_lit_pixels(G):
    pixels, (min_x, min_y, max_x, max_y) = G
    num = 0
    for (x, y) in pixels:
        if min_x <= x <= max_x and min_y <= y <= max_y:
            num += 1
    return num

def enhance(G):
    pixels, (min_x, min_y, max_x, max_y) = G
    enhanced = set()
    padding = MAX_ENHANCEMENT*2

    for x in range(min_x-1-padding, max_x+2+padding):
        for y in range(min_y-1-padding, max_y+2+padding):
            v = ''
            for xx, yy in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:
                v += '1' if (xx, yy) in pixels else '0'

            if algorithm_data[int(v, 2)] == '#':
                enhanced.add((x,y))

    return enhanced, (min_x-1, min_y-1, max_x+1, max_y+1)

pixels = set()
for ix, x in enumerate(image_data):
    for iy, y in enumerate(x):
        if y == '#':
            pixels.add((ix, iy))
image = (pixels, (0, 0, len(image_data), len(image_data[0])))

for i in range(1, MAX_ENHANCEMENT+1):
    image = enhance(image)

    if i == 2 or i == 50:
        print(count_lit_pixels(image))
