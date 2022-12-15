#!/usr/bin/env python3

data = open('in20.txt').read().split('\n\n')
algorithm_data = data[0]
image_data = [list(x) for x in data[1].splitlines()]

MAX_ENHANCEMENT = 100

def count_lit_pixels(G):
    pixels, (max_x, max_y, min_x, min_y) = G
    num = 0
    for (x, y) in pixels:
        if min_x <= x <= max_x and min_y <= y <= max_y:
            num += 1
    return num

def enhance(G):
    pixels, (max_x, max_y, min_x, min_y) = G
    enhanced = set()
    for x in range(min_x-1-MAX_ENHANCEMENT*2, max_x+2+MAX_ENHANCEMENT*2):
        for y in range(min_y-1-MAX_ENHANCEMENT*2, max_y+2+MAX_ENHANCEMENT*2):
            v = ''
            for xx, yy in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:
                v += '1' if (xx, yy) in pixels else '0'

            if algorithm_data[int(v, 2)] == '#':
                enhanced.add((x,y))

    return enhanced, (max_x+1, max_y+1, min_x-1, min_y-1) 

pixels = set()
max_x, max_y, min_x, min_y = len(image_data), len(image_data[0]), 0, 0

for ix, x in enumerate(image_data):
    for iy, y in enumerate(x):
        if y == '#':
            pixels.add((ix, iy))

image = (pixels, (max_x, max_y, min_x, min_y))

for i in range(MAX_ENHANCEMENT):
    image = enhance(image)
    if i+1 == 2 or i+1 == 50:
        print(count_lit_pixels(image))
