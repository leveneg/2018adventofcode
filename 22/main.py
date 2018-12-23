#! /usr/bin/env python3

import os
import sys

from collections import defaultdict
from functools import lru_cache
from heapq import heappush, heappop
from math import inf
from time import process_time

DEPTH = 6084
ORIGIN = (0, 0)
TARGET = (14, 709)

def main():
    target = TARGET[0] + TARGET[1] * 1j
    origin = ORIGIN[0] + ORIGIN[1] * 1j

    def getGi(p):
        if p in [origin, target]:
            return 0

        if p.imag == 0:
            return p.real * 16807

        if p.real == 0:
            return p.imag * 48271

        return getEl(p - 1) * getEl(p - 1j)

    # getEl is pure, so maxsize=None should be ok
    @lru_cache(maxsize=None)
    def getEl(p):
        return int((getGi(p) + DEPTH) % 20183)

    xr = range(int(origin.real), int(target.real) + 1)
    yr = range(int(origin.imag), int(target.imag) + 1)

    print('P1: {}'.format(sum(getEl(i + j * 1j) % 3 for i in xr for j in yr)))

    # complex doesn't support ordering, and heapq doesn't support custom
    # ordering, so split up components into floats for the heap :/
    queue = [(0, origin.real, origin.imag, 1)]
    weights = defaultdict(lambda: inf)

    while queue:
        m, x, y, t = heappop(queue)
        p = x + y * 1j
        key = (p, t)

        if weights[key] <= m:
            continue

        weights[key] = m

        if key == (target, 1):
            break

        # "z" neighbor(s)
        no = getEl(p) % 3
        for nt in range(3):
            if nt != t and nt != no:
                heappush(queue, (m + 7, x, y, nt))

        # x & y neighbor(s)
        for np in [p+1, p+1j, p-1, p-1j]:
            if np.real < 0 or np.imag < 0:
                continue

            if (getEl(np) % 3) == t:
                continue

            heappush(queue, (m + 1, np.real, np.imag, t))

    print('P2: {}'.format(weights[(target, 1)]))


if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
