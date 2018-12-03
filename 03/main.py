#! /usr/bin/env python3

import os
import sys
import time

from collections import defaultdict

def getClaims():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        for line in f:
            id, rest = line.strip().split(' @ ')
            origin, dims = rest.split(': ')

            x, y = [int(i) for i in origin.split(',')]
            dx, dy = [int(i) for i in dims.split('x')]

            yield (id, (x, y), (dx, dy))

def main():
    overlaps = {}
    claimed = defaultdict(list)

    for (id, (x, y), (dx, dy)) in getClaims():
        overlaps[id] = set()
        for i in range(x, x + dx):
            for j in range(y, y + dy):
                for n in claimed[(i, j)]:
                    overlaps[n].add(id)
                    overlaps[id].add(n)
                claimed[(i, j)].append(id)

    p1 = len([k for k in claimed if len(claimed[k]) > 1])
    p2 = [k for k in overlaps if len(overlaps[k]) == 0][0]

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = time.process_time()
    main()
    print('--- {} seconds ---'.format(time.process_time() - start))
