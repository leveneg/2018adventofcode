#! /usr/bin/env python3

import os
import sys

from collections import defaultdict
from math import inf
from time import process_time

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        exp = f.read().strip()

    p = 0
    stack = []
    distances = defaultdict(lambda: inf)
    distances[p] = 0
    dirs = {'E': 1, 'N': 1j, 'W': -1, 'S': -1j}
    for c in exp[1:-1]:
        if c == '(':
            stack.append(p)
            continue

        if c == ')':
            p = stack.pop()
            continue

        if c == '|':
            p = stack[-1]
            continue

        np = p + dirs[c]
        distances[np] = min(distances[np], distances[p] + 1)
        p = np

    vals = distances.values()

    print('P1: {}'.format(max(vals)))
    print('P2: {}'.format(len([x for x in vals if x >= 1000])))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
