#!/usr/bin/env python3

input = open('in6.txt', 'r').read().strip()

def find_marker(data, length):
    for i in range(len(data)):
        if len(set(input[i:i+length])) == length:
            return i + length

print(find_marker(input, 4))
print(find_marker(input, 14))
