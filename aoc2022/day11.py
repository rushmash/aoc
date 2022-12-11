#!/usr/bin/env python3

from functools import reduce
import re

input = [[y.strip() for y in x.splitlines()[1:]]
            for x in open('in11.txt', 'r').read().split('\n\n')]

mul = lambda x,y: x*y
MOD = 1

for monkey_note in input:
    MOD *= reduce(mul, map(int, re.findall('\d+', monkey_note[2])))

def simulate_keep_away_game(rounds, func):
    M = []
    I = []
    for monkey_note in input:
        M.append(list(map(int, re.findall('\d+', monkey_note[0]))))
        I.append(0)

    for _ in range(rounds):
        for monkey, items in enumerate(M):
            if not items:
                continue

            for monkey_note in input[monkey][1:]:
                match monkey_note.strip().split(':'):
                    case 'Operation', op:
                        rhs = op.removeprefix(' new = ')
                        f = lambda old: eval(rhs)

                        M[monkey] = list(map(lambda x: func(f(x)), M[monkey]))
                        I[monkey] += len(M[monkey])

                    case 'Test', op:
                        num = int(op.removeprefix(' divisible by '))

                    case 'If true', cmd:
                        to = int(cmd.removeprefix(' throw to monkey '))

                        keep = []
                        while M[monkey]:
                            v = M[monkey].pop()

                            if v % num == 0:
                                M[to].append(v)
                            else:
                                keep.append(v)
                        M[monkey].extend(keep)

                    case 'If false', cmd:
                        to = int(cmd.removeprefix(' throw to monkey '))

                        keep = []
                        while M[monkey]:
                            v = M[monkey].pop()

                            if v % num != 0:
                                M[to].append(v)
                            else:
                                keep.append(v)
                        M[monkey].extend(keep)
    return I


print(reduce(mul, sorted(simulate_keep_away_game(   20, lambda x: x // 3 ))[-2:]))
print(reduce(mul, sorted(simulate_keep_away_game(10000, lambda x: x % MOD))[-2:]))
