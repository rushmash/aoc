#!/usr/bin/env python3
from collections import defaultdict
from itertools import *
from typing import Counter

template = ''
rules = defaultdict(str)
with open('in14.txt', 'r') as f:
	template = f.readline().strip()
	f.readline()
	for line in f:
		(a1, a2), b = line.strip().split(' -> ')
		rules[(a1, a2)] = [(a1, b), (b, a2)]

def calculate(it):
	polymer = Counter(pairwise(template))
	for _ in range(it):
		to_add = Counter()
		for old, (new1, new2) in rules.items():
			count = polymer[old]
			to_add[new1] += polymer[old]
			to_add[new2] += polymer[old]
			del polymer[old]
		
		for (a, b), count in to_add.items():
			polymer[(a, b)] += count

	letters = Counter()
	for (a, b), count in polymer.items():
		letters[a] += count
		letters[b] += count

	letters2 = Counter()
	for a, c in letters.items():
		if a in [template[0], template[-1]] and template[0] != template[-1]:
			letters2[a] = (c + 1) // 2
		else:
			letters2[a] = c // 2

	mc = letters2.most_common()
	print(mc[0][-1] - mc[-1][-1])

def part1():
	calculate(10)

def part2():
	calculate(40)

part1()
part2()
