#!/usr/bin/env python3
from itertools import *

signals = []
digits = []
with open('in8.txt', 'r') as f:
	for line in f:
		s, d = line.strip().split("|")
		signals.append(s.strip().split())
		digits.append(d.strip().split())

def part1():
	return len(list(filter(lambda x: len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7, chain(*digits))))

def decode_signal(signal) -> list:
	decoded = [{} for _ in range(10)]

	while signal:
		signal_digit = signal.pop(0)
		code = set(signal_digit)
		digit = -1

		match len(code):
			case 2:
				decoded[1] = code
				digit = 1
			case 3:
				decoded[7] = code
				digit = 7
			case 4:
				decoded[4] = code
				digit = 4
			case 7:
				decoded[8] = code
				digit = 8

			case 5: # either 5,2,3

				# decode 5
				if decoded[3] and decoded[2]:
					decoded[5] = code
					digit = 5

				# decode 3
				elif decoded[1] and decoded[1].issubset(code):
					decoded[3] = code
					digit = 3

				# decode 2
				elif decoded[4] and decoded[6]:
					diff = decoded[6] - decoded[4]
					if diff.issubset(code):
						decoded[2] = code
						digit = 2

			case 6: # either 9,6,0

				# decode 9
				if decoded[3] and decoded[3].issubset(code):
					decoded[9] = code
					digit = 9
				elif decoded[4] and decoded[4].issubset(code):
					decoded[9] = code
					digit = 9

				# decode 6
				elif decoded[1] and not decoded[1].issubset(code):
					decoded[6] = code
					digit = 6

				# decode 0
				elif decoded[9]:
					if decoded[6] or decoded[1] and decoded[1].issubset(code):
						decoded[0] = code
						digit = 0

		if digit < 0:
			signal.append(signal_digit)

	return decoded

def decode_digit(digits, decoded_signal) -> int:
	digit_code = ''
	for digit in digits:
		for dec, di in zip(decoded_signal, count(0)):
			if set(digit) == dec:
				digit_code += str(di)
				break

	return int(digit_code)

def part2():
	value = 0
	for signal, digit in zip(signals, digits):
		decoded_signal = decode_signal(signal)
		value += decode_digit(digit, decoded_signal)

	return value


print(part1())
print(part2())
