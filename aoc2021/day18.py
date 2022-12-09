#!/usr/bin/env python3

from itertools import permutations
from math import ceil, floor
import re

input = open('in18.txt').read().splitlines()

def explode(s):
    while True:
        i1, i2 = 0, 0
        nesting = 0

        for i, v in enumerate(s):
            if v == '[':
                nesting += 1
                i1 = i
            elif v == ']':
                if nesting >= 5:
                    i2 = i + 1
                    break

                nesting -= 1
        else:
            return s

        if nesting >= 5:
            lv, rv = map(int, re.findall('\d+', s[i1:i2]))
            p1, p2 = s[:i1], s[i2:]

            if m := re.search('\d+(?!.*\d+)', p1):
                p1 = p1[:m.start()] + str(int(m.group(0))+lv) + p1[m.end():]

            if m := re.search('\d+', p2):
                p2 = p2[:m.start()] + str(int(m.group(0))+rv) + p2[m.end():]

            s = p1 + '0' + p2

def split(s):
    if m := re.search('\d{2}', s):
        p1, p2 = s[:m.start()], s[m.end():]
        v = int(s[m.start():m.end()]) / 2.0
        s = p1 + f'[{floor(v)},{ceil(v)}]' + p2
    return s

def magnitude(s):
    while m := re.search('\[\d+,\d+\]', s):
        lv, rv = map(int, re.findall('\d+', m.group(0)))
        p1, p2 = s[:m.start()], s[m.end():]
        s = p1 + str(3*lv + 2*rv) + p2
    return int(s)

def reduce(numbers):
    s = numbers[0]
    for num in numbers[1:]:
        s = f'[{s},{num}]'
        while True:
            v = split(explode(s))
            if v == s:
                break
            s = v
    return s

print(magnitude(reduce(input)))
print(max(map(lambda x: magnitude(reduce(x)), permutations(input, 2))))