#!/usr/bin/env python3

input = [[[int(z) for z in y.split('-')] \
                    for y in x.split(',')] \
                      for x in open('in4.txt', 'r').read().splitlines()]

r1, r2 = 0, 0
for line in input:
    p1, p2 = line
    a, b, c, d = *p1, *p2

    if c <= a <= d and \
       c <= b <= d or \
       a <= c <= b and \
       a <= d <= b:
        r1 += 1

    if c <= a <= d or \
       c <= b <= d or \
       a <= c <= b or \
       a <= d <= b:
        r2 += 1

print(r1)
print(r2)