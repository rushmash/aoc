#!/usr/bin/env python3
import re
import copy

def transpose(M):
    size = max([len(s) for s in M])
    T = [[] for _ in range(size)]

    for line in M:
        for vi, v in enumerate(line):
            if v:
                T[vi].append(v)

    return list(map(lambda x: list(reversed(x)), T))

data = open('in5.txt', 'r').read().split('\n\n')
data_stacks = data[0].splitlines()
data_instr  = data[1].splitlines()

p1 = re.compile('(\w)|\s{4}')
stacks = list(map(p1.findall, data_stacks))
stacks.pop()

stacks = transpose(stacks)

p2 = re.compile('\d+')
instructions = list(map(lambda x: list(map(int, p2.findall(x))), data_instr))

def stack_top(s) -> str:
    return ''.join(map(lambda x: x[-1], s))

def rearrange_part_one(s) -> str:
    for x, y, z in instructions:
        for _ in range(x):
            s[z-1].extend(s[y-1].pop())
    return stack_top(s)

def rearrange_part_two(s) -> str:
    for x, y, z in instructions:
        s[z-1].extend(s[y-1][-x:])
        del s[y-1][-x:]
    return stack_top(s)

print(rearrange_part_one(copy.deepcopy(stacks)))
print(rearrange_part_two(copy.deepcopy(stacks)))
