#!/usr/bin/env python3

import os
import sys

from itertools import accumulate, cycle
from time import process_time

def main():
    seen = set([0])
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        changes = [int(l) for l in f.readlines()]

    p1 = sum(changes)
    p2 = next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f))

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
