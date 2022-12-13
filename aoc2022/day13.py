#!/usr/bin/env python3

from functools import cmp_to_key

packets = [[eval(y) for y in x.splitlines()] for x in open('in13.txt', 'r').read().split('\n\n')]

def compare(lhs, rhs):
    if isinstance(lhs, int) and isinstance(rhs, int):
        if lhs < rhs:
            return 1
        elif lhs == rhs:
            return 0
        else:
            return -1

    elif isinstance(lhs, list) and isinstance(rhs, list):
        i = 0
        while i < len(lhs) and i < len(rhs):
            match compare(lhs[i], rhs[i]):
                case 1:
                    return 1
                case -1:
                    return -1
            i += 1

        if i == len(lhs) == len(rhs):
            return 0
        if i == len(lhs):
            return 1
        if i == len(rhs):
            return -1

        return 0

    elif isinstance(lhs, int) and isinstance(rhs, list):
        return compare([lhs], rhs)

    elif isinstance(lhs, list) and isinstance(rhs, int):
        return compare(lhs, [rhs])

    return True

flattened = []
res = []
for ip, pair in enumerate(packets, start=1):
    flattened.extend(pair)
    if compare(*pair) == 1:
        res.append(ip)

print(sum(res))

a = [[2]]
b = [[6]]
flattened.append(a)
flattened.append(b)

s = sorted(flattened, reverse=True, key=cmp_to_key(compare))
print((s.index(a)+1)*(s.index(b)+1))
