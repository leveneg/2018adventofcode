#! /usr/bin/env python3

import os
import sys

from functools import reduce
from itertools import combinations
from time import process_time

SERIAL = 7347
X_DIM = 300
Y_DIM = 300
MAX_SQUARE = 13

def main():
    def c(x, y):
        _id = x + 10
        p = (_id * y + SERIAL) * _id
        p = (p // 100 % 10) - 5

        return p

    m = [[c(x, y) for x in range(X_DIM)] for y in range(Y_DIM)]
    res = (None, None, None)

    for d in range(3, MAX_SQUARE):
        for y in range(Y_DIM - d):
            for x in range(X_DIM - d):
                p = sum([m[j][i] for i in range(x,x+d) for j in range(y,y+d)])
                if not res[1] or p > res[1]: res = ((x, y), p, d)

        if d == 3:
            p1 = str(res[0])

    p2 = str(res[0] + (res[2],))

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
