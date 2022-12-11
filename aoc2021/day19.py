#!/usr/bin/env python3

from itertools import *
import numpy as np

min_beacons_overlap = 12
scan_distance = 1000

reports = [np.asarray([np.asarray([int(z) \
                    for z in y.split(',')]) \
                        for y in x.splitlines()[1:]]) \
                            for x in open('in19.txt').read().split('\n\n')]

# https://stackoverflow.com/questions/16452383/70413438#70413438
R = []
for x, y, z in permutations([0, 1, 2]):
    for sx, sy, sz in product([-1, 1], repeat=3):
        rot = np.zeros((3,3))
        rot[0, x] = sx
        rot[1, y] = sy
        rot[2, z] = sz

        if np.linalg.det(rot) == 1:
            R.append(rot)

def match(r1, r2):
    score = 0
    offset = np.zeros((3))
    new = np.array((0))
    
    _sr1 = set([tuple(i) for i in r1])

    for v1 in r1:
        for v2 in r2:
            dx = v2 - v1
            _sr2 = set([tuple(i - dx) for i in r2])

            common = _sr1.intersection(_sr2)
            offset_score = len(common)

            if offset_score > score:
                score = offset_score
                offset = dx
                new = _sr2.difference(common)
                
    return (score, offset, np.asarray([*new]))

reports_rotations = [[[np.matmul(rot, v) for v in report] for rot in R] for report in reports]
report_offsets = [np.zeros((3)) for _ in range(len(reports))]
not_matched = [x for x in range(1, len(reports))]
point_cloud = reports_rotations[0][0]

while not_matched:
    nmi = not_matched.pop()

    for ri, report in enumerate(reports_rotations[nmi]):
        match_score, offset, new = match(point_cloud, report)

        if match_score >= min_beacons_overlap:
            report_offsets[nmi] = offset
            point_cloud = np.concatenate((point_cloud, new))

            print('left:', len(not_matched))
            break
    else:
        not_matched.insert(0, nmi)

print(len(point_cloud))

manhattan_distance = lambda a: int(sum(map(abs, a[0] - a[1])))
print(max(map(manhattan_distance, combinations(report_offsets, 2))))
