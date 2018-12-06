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
    counts = defaultdict(int)
    buff = 10000 // len(coords)
    minX = min(x for x, _ in coords)
    minY = min(y for _, y in coords)
    maxX = max(x for x, _ in coords)
    maxY = max(y for _, y in coords)

    for i in range(minX - buff, maxX + buff):
        for j in range(minY - buff, maxY + buff):
            dists = [((x, y), abs(x - i) + abs(y - j)) for x, y in coords]
            distSum = sum(dist for _, dist in dists)
            mDist = min(dists, key=lambda d: d[1])
            val = mDist if [d[1] for d in dists].count(mDist[1]) == 1 else (None, None)

            m[(i, j)] = val
            if distSum < 10000: in_region.add((i, j))

    for (x, y), (closest, dist) in m.items():
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
