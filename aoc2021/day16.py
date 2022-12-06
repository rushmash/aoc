#!/usr/bin/env python3
from functools import reduce

input = open('in16.txt').read().strip()
versions = []

def parse(data):
    if not '1' in data:
        return [], []

    version, type = int(data[:3], 2), int(data[3:6], 2)
    data = data[6:]

    versions.append(version)
    result = 0

    f = lambda x: x

    match type:
        case 0: # sum type
            f = lambda x, y: x + y
        case 1: # product type
            f = lambda x, y: x * y
        case 2: # min type
            f = lambda x, y: min(x, y)
        case 3: # max type
            f = lambda x, y: max(x, y)
        case 5: # greater type
            f = lambda x, y: 1 if x > y else 0
        case 6: # less than type
            f = lambda x, y: 1 if x < y else 0
        case 7: # equal type
            f = lambda x, y: 1 if x == y else 0

    match type:
        case 4: # literal type
            number = ''
            for i in range(0, len(data), 5):
                number += data[i+1: i+5]
                if data[i] == '0':
                    result = int(number, 2)
                    data = data[i+5:]
                    break

        case _: # any operator type
            length_type = data[:1]
            data = data[1:]

            match length_type:
                case '0':
                    length = int(data[:15], 2)
                    data = data[15:]

                    payload = data[:length]
                    data = data[length:]

                    result, payload = parse(payload)
                    while payload:
                        r, payload = parse(payload)
                        result = reduce(f, (result, r))

                case '1':
                    packets = int(data[:11], 2)
                    data = data[11:]

                    result, data = parse(data)
                    for _ in range(1, packets):
                        r, data = parse(data)
                        result = reduce(f, (result, r))

    return result, data

M = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

data = ''.join(map(lambda x: M[x], input))
value, _ = parse(data)

print(sum(versions))
print(value)