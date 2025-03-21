#!/usr/bin/env python3
from dataclasses import dataclass
from itertools import cycle, islice
from functools import cache

@dataclass(frozen=True)
class Player:
    score: int
    space: int

def take(n, iterable):
    return list(islice(iterable, n))

def dice(sides):
    for b in cycle(range(1, sides+1)):
        yield b

def part1(p1, p2):
    dice_roller = dice(100)
    turn = 0

    while True:
        new_p1_space = (sum(take(3, dice_roller)) + p1.space) % 10
        new_p1 = Player(p1.score + new_p1_space + 1, new_p1_space)
        turn += 3
        if new_p1.score >= 1000:
            return p2.score * turn

        p1, p2 = p2, new_p1

@cache
def part2(p1, p2):
    if p1.score >= 21:
        return (1, 0)

    if p2.score >= 21:
        return (0, 1)

    wins = (0, 0)
    for d1 in take(3, dice(3)):
        for d2 in take(3, dice(3)):
            for d3 in take(3, dice(3)):
                new_p1_space = (d1 + d2 + d3 + p1.space) % 10
                new_p1 = Player(p1.score + new_p1_space + 1, new_p1_space)

                s2, s1 = part2(p2, new_p1)
                wins = (wins[0] + s1, wins[1] + s2)
    return wins

data = open('aoc2021/in21.txt').read().splitlines()
data = [[int(w) for w in l.split() if w.isdigit()][1] for l in data]

print(part1(*[Player(0, p - 1) for p in data]))
print(max(part2(*[Player(0, p - 1) for p in data])))
