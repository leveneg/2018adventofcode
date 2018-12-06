#! /usr/bin/env python3

import os
import sys

from collections import defaultdict
from time import process_time

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        lines = [l.strip() for l in f.readlines()]
        coords = [tuple(int(n) for n in l.split(', ')) for l in lines]

    m = {}
    in_region = set()
    buff = 10000 // len(coords)
    xs, ys = zip(*coords)
    minX, minY, maxX, maxY = (min(xs), min(ys), max(xs), max(ys))

    for i in range(minX - buff, maxX + buff):
        for j in range(minY - buff, maxY + buff):
            _m = [((x, y), abs(x - i) + abs(y - j)) for x, y in coords]
            dists = [d for _, d in _m]
            distSum = sum(dists)
            mDist = min(_m, key=lambda d: d[1])

            m[(i, j)] = mDist[0] if dists.count(mDist[1]) == 1 else None
            if distSum < 10000: in_region.add((i, j))

    counts = defaultdict(int)
    for (x, y), closest in m.items():
        if not closest:
            continue

        if x <= minX or x >= maxX or y <= minY or y >= maxY:
            counts[closest] -= 2 ** 31

        counts[closest] += 1

    p1 = max(counts.values())
    p2 = len(in_region)

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
