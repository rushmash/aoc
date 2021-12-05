#!/usr/bin/env python3
from itertools import *

class Board:
	def __init__(self, arr) -> None:
		self.data = [list(zip(x, cycle([0]))) for x in arr]

	def mark_number(self, num):
		for l in self.data:
			for i in range(len(l)):
				d, m = l[i]
				if d == num:
					l[i] = (d, 1,)

	def won(self) -> bool:
		for l in self.data:
			if sum(map(lambda x: x[-1], l)) == len(l):
				return True

		for l in zip(*self.data):
			if sum(map(lambda x: x[-1], l)) == len(l):
				return True

		return False

	def get_unmarked(self) -> list:
		unmarked = []
		for l in self.data:
			for e in l:
				d, m = e
				if m == 0:
					unmarked.append(d)

		return unmarked

nums = []
boards = []

with open('in4.txt', 'r') as f:
	nums = [int(x) for x in f.readline().strip().split(',')]
	f.readline()
	data = []
	for line in f:
		l = line.strip().split()
		if len(l) > 0:
			data.append([int(x) for x in l])
		else:
			boards.append(Board(data))
			data = []

def part1() -> int:
	for n in nums:
		for b in boards:
			b.mark_number(n)
			if b.won():
				return n * sum(b.get_unmarked())

def part2() -> int:
	last_win_score = 0
	for n in nums:
		for b in boards:
			if b.won():
				continue

			b.mark_number(n)
			if b.won():
				last_win_score = n * sum(b.get_unmarked())

	return last_win_score

print(part1())
print(part2())
