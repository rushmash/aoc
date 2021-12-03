#!/usr/bin/env python3
from itertools import *

nums = [list(c.split()[0]) for c in open('in3.txt', 'r')]

def part1():
    bc = [x.count('1') for x in zip(*nums)]
    g = ''.join(map(lambda c: '1' if c > len(nums) / 2 else '0', bc))

    return int(g, 2) * (int(g, 2) ^ 0b111111111111)


def getNumber(most_common=False):
    v = nums[:]

    for i in range(len(nums[0])):
        onesCount = next(islice(zip(*v), i, i+1)).count('1')

        mostCommon  = lambda x, v=v, i=i: x[i] == ('1' if onesCount >= len(v) / 2 else '0')
        leastCommon = lambda x, v=v, i=i: x[i] == ('0' if onesCount >= len(v) / 2 else '1')

        v = list(filter(mostCommon if most_common else leastCommon, v))
        if len(v) == 1:
            break

    return ''.join(*v)

def part2():
    return int(getNumber(most_common=False), 2) * int(getNumber(most_common=True), 2)

print(part1())
print(part2())
