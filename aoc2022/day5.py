#!/usr/bin/env python3
import re
import copy

data = open('in5.txt', 'r').read().split('\n\n')
#data_stacks = data[0].splitlines()
data_instr  = data[1].splitlines()

# p1 = re.compile('\w')
# stacks = list(map(p1.findall, data_stacks))
# stacks.pop()

p2 = re.compile('\d+')
instructions = list(map(lambda x: list(map(int, p2.findall(x))), data_instr))

# [G]                 [D] [R]
# [W]         [V]     [C] [T] [M]
# [L]         [P] [Z] [Q] [F] [V]
# [J]         [S] [D] [J] [M] [T] [V]
# [B]     [M] [H] [L] [Z] [J] [B] [S]
# [R] [C] [T] [C] [T] [R] [D] [R] [D]
# [T] [W] [Z] [T] [P] [B] [B] [H] [P]
# [D] [S] [R] [D] [G] [F] [S] [L] [Q]
#  1   2   3   4   5   6   7   8   9

stacks = [
    ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'],
    ['S', 'W', 'C'],
    ['R', 'Z', 'T', 'M'],
    ['D', 'T', 'C', 'H', 'S', 'P', 'V'],
    ['G', 'P', 'T', 'L', 'D', 'Z'],
    ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'],
    ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R'],
    ['L', 'H', 'R', 'B', 'T', 'V', 'M'],
    ['Q', 'P', 'D', 'S', 'V']
]

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
