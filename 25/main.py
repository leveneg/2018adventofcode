#! /usr/bin/env python3

import os
import sys

from time import process_time

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        lines = [l.strip() for l in f.readlines()]
        coords = [tuple(int(c) for c in l.split(',')) for l in lines]

    ns = [set() for _ in range(len(coords))]
    for i, f in enumerate(coords):
        for j, s in enumerate(coords):
            if sum(abs(b - a) for a, b in zip(f, s)) <= 3:
                ns[i].add(j)

    consts = set()
    result = 0

    for i in range(len(ns)):
        if i in consts: continue

        result += 1

        queue = [i]
        while queue:
            n = queue.pop(0)
            if n in consts:
                continue

            consts.add(n)
            queue += ns[n]

    print('P1: {}'.format(result))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
