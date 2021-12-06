#!/usr/bin/env python3
from collections import defaultdict
from itertools import *

class Point:
	def __init__(self, x, y) -> None:
		self.x = x
		self.y = y

	def __hash__(self) -> int:
		return hash((self.x, self.y))

	def __eq__(self, other) -> bool:
		return self.x == other.x and self.y == other.y

class LineSegment:
	def __init__(self, x1, y1, x2, y2) -> None:
		self.p1 = Point(x1, y1)
		self.p2 = Point(x2, y2)

	def horizontal(self) -> bool:
		return self.p1.y == self.p2.y

	def vertical(self) -> bool:
		return self.p1.x == self.p2.x

	def points(self) -> list:
		points = []

		step_x = 1 if self.p1.x <= self.p2.x else -1
		step_y = 1 if self.p1.y <= self.p2.y else -1

		if self.vertical():
			for y in range(self.p1.y, self.p2.y+step_y, step_y):
				points.append(Point(self.p1.x, y))
			return points

		if self.horizontal():
			for x in range(self.p1.x, self.p2.x+step_x, step_x):
				points.append(Point(x, self.p1.y))
			return points

		for x, y in zip(range(self.p1.x, self.p2.x+step_x, step_x), range(self.p1.y, self.p2.y+step_y, step_y)):
			points.append(Point(x, y))

		return points


vent_segments = []
with open('in5.txt', 'r') as f:
	for line in f:
		t1, t2 = line.strip().split(' -> ')
		p1 = [int(x) for x in t1.split(',')]
		p2 = [int(x) for x in t2.split(',')]
		vent_segments.append(LineSegment(*(p1 + p2)))


def part1() -> int:
	intersection_count = defaultdict(int)

	for s in filter(lambda s: s.horizontal() or s.vertical(), vent_segments):
		for p in s.points():
			intersection_count[p] += 1

	return len(list(filter(lambda v: v[1] >= 2, intersection_count.items())))

def part2() -> int:
	intersection_count = defaultdict(int)

	for s in vent_segments:
		for p in s.points():
			intersection_count[p] += 1

	return len(list(filter(lambda v: v[1] >= 2, intersection_count.items())))


print(part1())
print(part2())