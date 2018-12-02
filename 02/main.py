#! /usr/bin/env python3

import os
import sys

from functools import reduce
from itertools import combinations

def getLines():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        return [l.strip() for l in f.readlines()]

def p1(ids):
    return reduce(
        lambda x, y: x * y,
        [sum(1 for l in ids if any(l.count(c) == x for c in l)) for x in (2,3)]
    )

def p2(ids):
    for first, second in combinations(ids, 2):
        z = list(zip(first, second))
        if sum([1 for f, s in z if f != s]) == 1:
            return ''.join([f for f, s in z if f == s])

def main():
    ids = getLines()

    print('P1: {}'.format(p1(ids)))
    print('P2: {}'.format(p2(ids)))

if __name__ == "__main__":
    main()
