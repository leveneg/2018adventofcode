#! /usr/bin/env python3

import os
import sys

from time import process_time

GENERATIONS = 50000000000

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        lines = [l.strip() for l in f.readlines()]
        _, init = [s for s in lines[0].split(': ')]
        state = [i for i, s in enumerate(init) if s == '#']
        rules = {f: s for f, s in [l.split(' => ') for l in lines[2:]]}

    ls, ld = (sum(state), 0)
    matched_once = False
    for i in range(GENERATIONS):
        ns = set()
        for j in range(min(state) - 2, max(state) + 3):
            local = ''.join('#' if j + k in state else '.' for k in range(-2,3))
            if rules[local] == '#': ns.add(j)

        state = ns
        res = sum(state)

        if i == 19:
            p1 = res

        if res - ls == ld:
            if matched_once:
                p2 = ((GENERATIONS - i - 1) * ld) + res
                matched_once = False
                break

            matched_once = True
        else:
            matched_once = False

        ls, ld = (res, res - ls)

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
