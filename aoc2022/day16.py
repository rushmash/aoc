#!/usr/bin/env python3

from collections import deque, defaultdict
from itertools import combinations
import re

valve_bitmask = {}
valve_rates = {}
valve_transitions = {}
for i, line in enumerate(open('in16.txt', 'r').read().splitlines()):
	tunnels = re.findall('[A-Z]{2}', line)
	valve_transitions[tunnels[0]] = tunnels[1:]
	if flow_rate := int(re.findall('\d+', line)[0]):
		valve_rates[tunnels[0]] = flow_rate
		valve_bitmask[tunnels[0]] = 1 << len(valve_bitmask)

def bfs(graph, max_budget):
	# path budget, opened valves, current valve, total rate
	Q = deque([(0, 0, 'AA', 0)])
	S = set()
	paths = defaultdict(int)

	while Q:
		budget, opened, current, total = Q.pop()
		paths[opened] = max(paths[opened], total)
		if budget == max_budget:
			continue

		if (opened, current) in S:
			continue

		S.add((opened, current))
		if current in valve_rates and not opened & valve_bitmask[current]:
			valve_score = valve_rates[current] * (max_budget - budget - 1)
			Q.appendleft((budget + 1, opened | valve_bitmask[current], current, total + valve_score))

		for adjacent in graph[current]:
			Q.appendleft((budget + 1, opened, adjacent, total))

	return paths

paths = bfs(valve_transitions, 30)
print(max(paths.values()))

max_pressure = 0
paths = bfs(valve_transitions, 26)
for (p1, v1), (p2, v2) in combinations(paths.items(), 2):
	if p1 and p2 and not p1 & p2:
		max_pressure = max(max_pressure, v1 + v2)

print(max_pressure)
