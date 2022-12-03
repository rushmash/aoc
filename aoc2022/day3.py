#!/usr/bin/env python3

input = open('in3.txt', 'r').read().splitlines()

r = 0
for line in input:
    i = len(line)//2
    x, y = line[:i], line[i:]
    c = set(x).intersection(y).pop()
    if c.isupper():
        r += ord(c) - 38
    else:
        r += ord(c) - 96

print(r)

r = 0
it = iter(input)
for i in range(len(input)//3):
    x, y, z = next(it), next(it), next(it)
    c = set(x).intersection(y).intersection(z).pop()
    if c.isupper():
        r += ord(c) - 38
    else:
        r += ord(c) - 96

print(r)