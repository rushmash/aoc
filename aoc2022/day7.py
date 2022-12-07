#!/usr/bin/env python3

import os.path
from collections import defaultdict

input = open('in7.txt', 'r').read().splitlines()

wd = '/'
files = []
for line in input:
    match line.split():
        case '$', 'cd', arg:
            wd += arg + '/'
        case '$', _:
            pass
        case 'dir', _:
            pass
        case size, name:
            path = os.path.normpath(wd + name)
            files.append((path, int(size)))

dirs = defaultdict(int)
for path, size in files:
    dir_name = os.path.dirname(path)

    while True:
        dirs[dir_name] += size
        if dir_name == os.path.dirname(dir_name):
            break

        dir_name = os.path.dirname(dir_name)

print(sum(filter(lambda x: x < 100000, dirs.values())))

disk = 70000000
required = 30000000
to_free = required - (disk - dirs['/'])

print(min(filter(lambda x: x > to_free, dirs.values())))