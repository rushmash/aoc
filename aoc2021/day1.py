#!/usr/bin/env python3

nums = [int(n) for n in open('in1.txt', 'r')]

def part1():
    count = 0

    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            count += 1

    return count

def part2():
    count = 0

    for i in range(3, len(nums)):
        s0 = nums[i-3] + nums[i-2] + nums[i-1]
        s1 = nums[i-2] + nums[i-1] + nums[i]
        if s1 > s0:
            count += 1

    return count

print(part1())
print(part2())
