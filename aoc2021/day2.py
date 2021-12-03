#!/usr/bin/env python3

cmds = [c.split() for c in open('in2.txt', 'r')]

def part1():
    xPos, yPos = 0, 0

    for cmd, d in cmds:
        match cmd:
            case 'forward':
                xPos += int(d)
            case 'down':
                yPos += int(d)
            case 'up':
                yPos -= int(d)

    return xPos * yPos

def part2():
    xPos, yPos, aim = 0, 0, 0

    for cmd, d in cmds:
        match cmd:
            case 'forward':
                xPos += int(d)
                yPos += aim * int(d)
            case 'down':
                aim += int(d)
            case 'up':
                aim -= int(d)

    return xPos * yPos

print(part1())
print(part2())
