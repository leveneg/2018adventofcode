#! /usr/bin/env python3

import os
import sys

from copy import deepcopy
from time import process_time
from string import ascii_uppercase as uppers

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        instructions = [l.strip().split(' ') for l in f.readlines()]
        deps = [(l[1], l[7]) for l in instructions]

    nNodes = len(uppers)
    steps = []
    g = {k: [0 for _ in range(nNodes)] for k in uppers}
    for dep, step in deps:
        g[step][uppers.index(dep)] = 1

    m = deepcopy(g)
    while len(steps) < nNodes:
        nextStep = next(s for s, d in m.items() if not any(d) and s not in steps)
        steps.append(nextStep)
        del m[nextStep]
        for deps in m.values(): deps[uppers.index(nextStep)] = 0

    p1 = ''.join(steps)

    m = deepcopy(g)
    tasks = []
    tick = 0
    while tasks or m:
        tNames, times = zip(*tasks) if tasks else ([], [])
        avail = [t for t, d in m.items() if t not in tNames and not any(d)]

        if avail and len(tasks) < 5:
            tName = min(avail)
            tasks.append((tName, ord(tName) - 4))
            continue

        mTime = min(times)
        done = [(t, tt) for t, tt in tasks if tt == mTime]
        tasks = [(t, tt - mTime) for t, tt in tasks if (t, tt) not in done]
        tick += mTime

        for s, _ in done:
            for r in m.values(): r[uppers.index(s)] = 0
            del m[s]

    p2 = tick

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
