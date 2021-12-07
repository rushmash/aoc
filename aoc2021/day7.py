#!/usr/bin/env python3
import sys

positions = []
with open('in7.txt', 'r') as f:
	positions = [int(pos) for pos in f.readline().strip().split(',')]

def get_min_fuel(calc_rule):
	min_fuel = sys.maxsize
	for i in range(min(positions), max(positions)+1):
		ifuel = 0
		for p in positions:
			ifuel += calc_rule(i, p)
		if min_fuel > ifuel:
			min_fuel = ifuel
	return min_fuel

def part1():
	return get_min_fuel(lambda x, y: abs(x - y))

def part2():
	return get_min_fuel(lambda x, y: (abs(x - y) + 1)**2 // 2 - (abs(x - y) + 1) // 2)

print(part1())
print(part2())
