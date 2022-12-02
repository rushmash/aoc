#!/usr/bin/env python3

input = [[int(y) for y in x.split('\n')] for x in open('in1.txt', 'r').read().split('\n\n')]

sums = sorted(map(sum, input))

print(sums[-1])
print(sum(sums[-3:]))
