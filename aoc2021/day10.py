#!/usr/bin/env python3
from itertools import *
from collections import deque

lines = [l.strip() for l in open('in10.txt', 'r')]

score_points1 = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137,
}

score_points2 = {
	')': 1,
	']': 2,
	'}': 3,
	'>': 4,
}

token_pair = {
	')': '(',
	']': '[',
	'}': '{',
	'>': '<',
	'(': ')',
	'[': ']',
	'{': '}',
	'<': '>',
}

def part1():
	score = 0
	for line in lines:
		brackets = deque()
		for token in line:
			if token in ['(', '[', '{', '<']:
				brackets.append(token)
			elif token in [')', ']', '}', '>']:
				if token_pair[token] != brackets.pop():
					score += score_points1[token]
					break
	return score

def get_incomplete_brackets(line):
	brackets = deque()
	for token in line:
		if token in ['(', '[', '{', '<']:
			brackets.append(token)
		elif token in [')', ']', '}', '>']:
			if token_pair[token] != brackets.pop():
				return []
	return brackets

def part2():
	scores = []
	for line in lines:
		score = 0
		brackets = get_incomplete_brackets(line)
		if not brackets:
			continue

		for b in reversed(brackets):
			score *= 5
			score += score_points2[token_pair[b]]
		scores.append(score)

	return sorted(scores)[len(scores)//2]

print(part1())
print(part2())
