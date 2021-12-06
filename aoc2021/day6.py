#!/usr/bin/env python3
from collections import defaultdict

fish = []
with open('in6.txt', 'r') as f:
	fish = [int(age) for age in f.readline().strip().split(',')]

def get_fish_population(days) -> int:
	model = defaultdict(int)
	for age in fish:
		model[age] += 1

	for _ in range(days):
		new_population = defaultdict(int)
		for age, fish_count in model.items():
			if age > 0:
				new_population[age - 1] += fish_count
			elif age == 0:
				new_population[8] += fish_count
				new_population[6] += fish_count
		model = new_population

	return sum(list(map(lambda x: x[1], model.items())))

def part1():
	return get_fish_population(80)

def part2():
	return get_fish_population(256)

print(part1())
print(part2())