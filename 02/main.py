#! /usr/bin/env python3

import os
import sys

from functools import reduce
from itertools import combinations
from time import process_time

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        ids = [l.strip() for l in f.readlines()]

    p1 = reduce(
        lambda x, y: x * y,
        [sum(1 for l in ids if any(l.count(c) == x for c in l)) for x in (2,3)]
    )

    for first, second in combinations(ids, 2):
        z = list(zip(first, second))
        if sum(1 for f, s in z if f != s) == 1:
            p2 = ''.join(f for f, s in z if f == s)
            break

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
