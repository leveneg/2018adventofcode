#! /usr/bin/env python3

import os
import sys

from time import process_time
from string import ascii_uppercase as uppers

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        instructions = [l.strip().split(' ') for l in f.readlines()]
        deps = [(l[1], l[7]) for l in instructions]

    steps = []
    g = {k: [d for d, s in deps if s == k] for k in uppers}
    while len(steps) < len(uppers):
        ns = next(s for s, d in g.items() if s not in steps and all(p in steps for p in d))
        steps.append(ns)

    p1 = ''.join(steps)

    tick = 0
    steps = tasks = []
    while len(steps) < len(uppers):
        names, times = zip(*tasks) if tasks else ([], [])
        ns = next(s for s, d in g.items() if s not in steps + list(names) and all(p in steps for p in d))

        if ns and len(tasks) < 5:
            tasks.append((ns, ord(ns) - 4))
            continue

        mTime = min(times)
        done = [t for t, tt in tasks if tt == mTime]
        tasks = [(t, tt - mTime) for t, tt in tasks if t not in done]
        tick += mTime
        steps += done

    p2 = tick

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
