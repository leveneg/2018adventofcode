#!/usr/bin/env python3

import os
import sys

from itertools import accumulate, cycle

def getLines():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        return f.readlines()

def p1(changes):
    return sum(changes)

def p2(changes):
    seen = set([0])
    return next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f))

def main():
    changes = [int(l) for l in getLines()]

    print('P1: {}'.format(p1(changes)))
    print('P2: {}'.format(p2(changes)))

if __name__ == "__main__":
    main()
