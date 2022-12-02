#!/usr/bin/env python3

input = open('in2.txt', 'r').read().splitlines()

#  A for Rock, B for Paper, and C for Scissors
#  X for Rock, Y for Paper, and Z for Scissors
score = 0
for e in input:
    match e:
        case 'A X':
            score += 1 + 3
        case 'A Y':
            score += 2 + 6
        case 'A Z':
            score += 3 + 0
        case 'B X':
            score += 1 + 0
        case 'B Y':
            score += 2 + 3
        case 'B Z':
            score += 3 + 6
        case 'C X':
            score += 1 + 6
        case 'C Y':
            score += 2 + 0
        case 'C Z':
            score += 3 + 3

print(score)

# X lose, Y a draw, Z win
score = 0
for e in input:
    match e:
        case 'A X':
            score += 3 + 0
        case 'A Y':
            score += 1 + 3
        case 'A Z':
            score += 2 + 6
        case 'B X':
            score += 1 + 0
        case 'B Y':
            score += 2 + 3
        case 'B Z':
            score += 3 + 6
        case 'C X':
            score += 2 + 0
        case 'C Y':
            score += 3 + 3
        case 'C Z':
            score += 1 + 6

print(score)
