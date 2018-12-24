#! /usr/bin/env python3

import os
import sys

from time import process_time

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        lines = [l.strip() for l in f.readlines()]

    bots = []
    for line in lines:
        pstr, rstr = line.split(', ')
        x, y, z = [int(s) for s in pstr.split('=')[1].strip('<>').split(',')]
        r = int(rstr.split('=')[1])
        bots.append((x, y, z, r))

    bb = max(bots, key=lambda b: b[3])

    c = 0
    for bot in bots:
        if sum(abs(b - a) for a, b in zip(bot[:3], bb[:3])) < bb[3]:
            c += 1

    print('P1: {}'.format(c))

    # we only really care about distance from 0, so map everything to that
    queue = []
    for x, y, z, r in bots:
        d = abs(x) + abs(y) + abs(z)
        queue.append((max(0, d - r), 1))
        queue.append((d + r, -1))

    queue = sorted(queue)

    res = 0
    c = 0
    mc = c
    while queue:
        dist, e = queue.pop(0)
        c += e

        if c > mc:
            res = dist
            mc = c

    print('P2: {}'.format(res))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
