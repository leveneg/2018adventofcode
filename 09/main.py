#! /usr/bin/env python3

import os
import sys

from collections import deque, defaultdict
from time import process_time

NUM_PLAYERS = 459
LAST_POINT = 71790

def main():
    ps = defaultdict(int)
    c = deque([0])

    for i in range(1, LAST_POINT * 100 + 1):
        if i % 23 == 0:
            c.rotate(7)
            ps[i % NUM_PLAYERS] += i + c.pop()
            c.rotate(-1)
            continue

        c.rotate(-1)
        c.append(i)

        if i == LAST_POINT + 1:
            p1 = max(ps.values())

    p2 = max(ps.values())

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
