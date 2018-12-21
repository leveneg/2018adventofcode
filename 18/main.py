#! /usr/bin/env python3

import os
import sys

from time import process_time

SHOW_ANIMATION = True
GENERATIONS = 1000000000

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        m = [list(l.strip()) for l in f.readlines()]

    p1 = p2 = None
    dirs = [1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j]
    mp = max(len(l) for l in m) + len(m) * 1j

    def it(p):
        neighbors = []
        x, y = int(p.real), int(p.imag)
        for d in dirs:
            i, j = int(x + d.real), int(y + d.imag)
            if not (0 <= i < mp.real) or not (0 <= j < mp.imag):
                continue

            neighbors.append(m[j][i])

        tile = m[y][x]
        nt, no, nl = [neighbors.count(c) for c in ['|', '.', '#']]

        if tile == '.':
            return '|' if nt > 2 else tile

        if tile == '|':
            return '#' if nl > 2 else tile

        if tile == '#':
            return tile if nl > 0 and nt > 0 else '.'


    rvs = []
    mod = None
    for tick in range(GENERATIONS):
        if SHOW_ANIMATION:
            os.system('clear')
            for r in m:
                print(''.join(r))

        _m = [r[:] for r in m]

        for j in range(int(mp.imag)):
            for i in range(int(mp.real)):
                _m[j][i] = it(i + j * 1j)

        m = _m

        flatm = [c for r in m for c in r]
        rv = flatm.count('|') * flatm.count('#')
        rvs.append(rv)

        if tick == 10 - 1:
            p1 = rv

        if mod and ((tick + 1) % mod == (GENERATIONS % mod)):
            p2 = rv
            break

        if len(rvs) < 100:
            continue

        dup = next((i for i, v in enumerate(rvs) if v == rvs[0]), None)
        if dup and all(rvs[dup+i+1] == rvs[i] for i in range(15)):
            mod = dup + 1


    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
